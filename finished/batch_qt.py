#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import glob, base64, re, pexpect, redis, os

# Import custom widget
from seq_scn_shot import Ui_Form

exr_path = "/nas/projects/Tactic/bilal/render/XXX/YYY/ZZZ/comp/render/exr/VVV/XXX_YYY_ZZZ_cmp_compositing_VVV.%04d.exr"
mov_path = "/nas/projects/Tactic/bilal/render/{0}/{1}/{2}/comp/render/mov/{3}/"

class SeqScnShot(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        QWidget.__init__(self, parent)

        self.ui = Ui_Form()

        print >>sys.stderr, kwargs.get('item_count')

        self.ui.setupUi(self, **kwargs)

class Widget(QWidget):
    item_count = 1
    seq_scn_shot_items = []
    djv_cmd = "/usr/bin/djv_convert {0} {1} -ffmpeg_format mjpeg"

    def __init__(self, parent= None):
        super(Widget, self).__init__()

        # Add a button and connect it to its slot
        #btn_new = QPushButton("Input More")
        #self.connect(btn_new, SIGNAL('clicked()'), self.add_new_custom_widget)
        # Add a button and connect it to its slot
        btn_batch = QPushButton("Batch Convert")
        self.connect(btn_batch, SIGNAL('clicked()'), self.batch_process)

        # the main widget
        self.widget = QWidget()
        # Add a vertical layout
        layout = QVBoxLayout(self)
        # Add a text line and disable it
        seq_scn_shot_obj = SeqScnShot(item_count=self.__class__.item_count)
        self.__class__.seq_scn_shot_items.append(seq_scn_shot_obj)
        self.__class__.item_count += 1

        layout.addWidget(seq_scn_shot_obj)
        layout.addStretch()

        # Add the layout to the widget
        self.widget.setLayout(layout)

        # Declare a QSrollArea and add the widget to it.
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # Make it resizable
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.widget)

        # The main window vertical layout
        vLayout = QVBoxLayout(self)
        # Add process button to it
        #vLayout.addWidget(btn_new)
        # Add scroll to it
        vLayout.addWidget(scroll)
        # Set this as the main widget layout
        self.setLayout(vLayout)
        # Add process button to it
        vLayout.addWidget(btn_batch)

    def add_new_custom_widget(self):
        seq_scn_shot_obj = SeqScnShot(item_count=self.__class__.item_count)
        self.__class__.seq_scn_shot_items.append(seq_scn_shot_obj)
        self.__class__.item_count += 1

        #seq_scn_shot_obj = MyWin().show()
        self.widget.layout().insertWidget(self.widget.layout().count() - 1, seq_scn_shot_obj)

    def batch_process(self):
        self.paths = []
        for item in self.__class__.seq_scn_shot_items:
            ver_paths = []
            if not item.ui.disqualify:
                seq = str(item.ui.sequence_comboBox_obj.currentText()).encode('ascii')
                scn = str(item.ui.scene_comboBox_obj.currentText()).encode('ascii')
                shot = str(item.ui.shot_comboBox_obj.currentText()).encode('ascii')
                ver = str(item.ui.version_comboBox_obj.currentText()).encode('ascii')

                shots = []
                if shot == '<All>':
                    sobjectSeq = item.ui.__class__.userQuery.getSeqSObjectbyName(seq)
                    if sobjectSeq:
                        sobjectSeq = sobjectSeq[0]['code'].encode('ascii')
                        sobjectScn = item.ui.__class__.userQuery.getScnSObjectbyNameAndSeqCode(scn, sobjectSeq)
                        if sobjectScn:
                            sobjectShots = item.ui.__class__.userQuery.getShtSObjectbyName(sobjectSeq, sobjectScn[0]['code'])
                            if sobjectShots:
                                for shot in sobjectShots:
                                    shots.append(shot['name'])
                else:
                    shots.append(shot)

                if ver == '<All>':
                    for shot in shots:
                        path = item.ui.__class__.base_path + item.ui.__class__.rel_exr_path
                        path = path.format(seq, scn, shot)
                        #print path

                        paths = sorted(glob.glob(path))
                        for path in paths:
                            #print path
                            ver_paths.append(path)
                elif ver == '<Latest>':
                    for shot in shots:
                        path = item.ui.__class__.base_path + item.ui.__class__.rel_exr_path
                        path = path.format(seq, scn, shot)
                        #print path

                        paths = sorted(glob.glob(path))
                        ver_paths.append(paths[-1])
                else:
                    path = item.ui.__class__.base_path + item.ui.__class__.rel_exr_abs_path
                    path = path.format(seq, scn, shot, ver)
                    #print path
                    ver_paths.append(path)
            else:
                path = str(item.ui.file_path_obj.text()).encode('ascii')
                if path:
                    ver_paths.append(path)

            if ver_paths:
                self.paths.append((item, ver_paths))

        self.djv()

    def djv(self):
        print self.paths
        """
        for item, ver_paths in self.paths:
            item.ui.status_message_obj.clear()
            print item.ui.uuid4

            size = len(ver_paths)
            step = 100 / size
            progress_percent = 0
            count = 0
            frontend_key = str(item.ui.uuid4)
            coll_val = ""
            for path in ver_paths:
                exr_wc = path + "/*"
                images = sorted(glob.glob(exr_wc))
                if images:
                    print images[0]

                    try:
                        (prefix, first, suffix) =  re.search("(.*\.)([0-9]+)(\.exr)", images[0]).groups()
                        last =  re.search("(.*\.)([0-9]+)(\.exr)", images[-1]).groups()[1]
                        input_path = prefix + first + "-" + last + suffix

                        (base_path, render_ver) = re.search("(.*render)/exr/(v\d{1,})", path).groups()
                        output_path = "{0}/mov/{1}".format(base_path, render_ver)
                        os.makedirs(output_path)

                        djv_cmd = self.__class__.djv_cmd.format(input_path, output_path)

                        coll_val += djv_cmd + ":::"
                        print djv_cmd
                    except Exception as e:
                        print e.message
                        item.ui.status_message_obj.appendPlainText("Error: {0}".format(e.message))

            #print "STR: ", collective_string
            encoded = base64.b64encode(coll_val)
            # open redis database and put the encoded string into it
            hset_key = "djv::{0}".format(frontend_key)
            try:
                r_server = redis.Redis("lic", port=4444, db=1)
                # hset
                res = r_server.hset(hset_key, "args", encoded)
                print "Added hash: ", res
                # set
                res = r_server.sadd("djv_items", hset_key)
                print "Added set: ", res
            except Exception as e:
                print e.message
                item.ui.status_message_obj.appendPlainText("Error: {0}".format(e.message))

        return
        """

        for item, ver_paths in self.paths:
            item.ui.status_message_obj.clear()

            size = len(ver_paths)
            step = 100 / size
            progress_percent = 0
            count = 0
            for path in ver_paths:
                exr_wc = path + "/*"
                images = sorted(glob.glob(exr_wc))
                if images:
                    #print images[0]
                    try:
                        (prefix, first, suffix) =  re.search("(.*\.)([0-9]+)(\.exr)", images[0]).groups()
                        last =  re.search("(.*\.)([0-9]+)(\.exr)", images[-1]).groups()[1]
                        input_path = prefix + first + "-" + last + suffix

                        #output_path = "/tmp/foo{0}.mov".format(count+1)

                        (_seq, _scn, _shot, _ver) = re.search(".*?(seq\d{1,}[a-zA-Z]{0,})/(scn\d{1,}[a-zA-Z]{0,})/(sh\d{1,}[a-zA-Z]{0,}).*?(v\d{1,})", path).groups()
                        output_path = mov_path.format(_seq, _scn, _shot, _ver)
                        print output_path
                        #(base_path, render_ver) = re.search("(.*render)/exr/(v\d{1,})", path).groups()
                        #output_path = "{0}/mov/{1}/".format(base_path, render_ver)
                        if not os.path.exists(output_path):
                            os.makedirs(output_path)

                        output_file = "{0}_{1}_{2}_{3}.mov".format(_seq, _scn, _shot, _ver)
                        output_path += output_file

                        djv_cmd = self.__class__.djv_cmd.format(input_path, output_path)

                        print djv_cmd

                        thread = pexpect.spawn(djv_cmd)
                        cpl = thread.compile_pattern_list([pexpect.EOF, '(.*)'])

                        while True:
                            i = thread.expect_list(cpl, timeout=None)
                            if i == 0:
                                break
                            elif i == 1:
                                progress_output = thread.match.group(1).strip()
                                print progress_output
                                item.ui.status_message_obj.appendPlainText(progress_output)
                                try:
                                    progress_stat_reg_ex = re.search("^\[\s?(\d+)%\]", progress_output)
                                    if progress_stat_reg_ex:
                                        progress_stat = count * step + float(progress_stat_reg_ex.groups()[0]) / size
                                        print progress_stat
                                        item.ui.progress_bar_obj.setValue(int(progress_stat))
                                except Exception as e:
                                    #print e.message
                                    item.ui.status_message_obj.appendPlainText("Error: {0}".format(e.message))
                        count += 1

                        #item.ui.progress_bar_obj.setValue(100)
                        thread.close()
                    except Exception as e:
                        print e.message
                        item.ui.status_message_obj.appendPlainText("Error: {0}".format(e.message))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialog = Widget()
    dialog.show()

    app.exec_()
