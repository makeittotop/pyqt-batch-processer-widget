# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seq_scn_shot.ui'
#
# Created: Wed Jun 17 13:33:36 2015
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys
sys.path.append("/nas/projects/development/productionTools/assetPublisher/tactic_modules/")
import queryClass as qClass
import getTicket as serverSetup
import glob
import uuid
import re

class Ui_Form(object):
    userQuery = None
    ticket = None
    sequences = []
    base_path = "/nas/projects/Tactic/bilal/render/"
    rel_exr_path = "{0}/{1}/{2}/comp/render/exr/v*"
    rel_exr_abs_path = "{0}/{1}/{2}/comp/render/exr/{3}"

    def setupUi(self, Form, **kwargs):
        Form.setObjectName("Form")
        Form.resize(653, 363)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtGui.QFrame(Form)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input_obj = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_obj.sizePolicy().hasHeightForWidth())
        self.input_obj.setSizePolicy(sizePolicy)
        self.input_obj.setObjectName("input_obj")
        self.gridLayout_2.addWidget(self.input_obj, 0, 1, 1, 1)
        self.seq_obj = QtGui.QLabel(self.frame)
        self.seq_obj.setObjectName("seq_obj")
        self.gridLayout_2.addWidget(self.seq_obj, 1, 1, 1, 1)
        self.scn_obj = QtGui.QLabel(self.frame)
        self.scn_obj.setObjectName("scn_obj")
        self.gridLayout_2.addWidget(self.scn_obj, 2, 1, 1, 1)
        self.shot_obj = QtGui.QLabel(self.frame)
        self.shot_obj.setObjectName("shot_obj")
        self.gridLayout_2.addWidget(self.shot_obj, 3, 1, 1, 1)
        self.version_obj = QtGui.QLabel(self.frame)
        self.version_obj.setObjectName("version_obj")
        self.gridLayout_2.addWidget(self.version_obj, 4, 1, 1, 1)
        self.path_obj = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_obj.sizePolicy().hasHeightForWidth())
        self.path_obj.setSizePolicy(sizePolicy)
        self.path_obj.setObjectName("path_obj")
        self.gridLayout_2.addWidget(self.path_obj, 5, 1, 1, 1)
        self.file_path_obj = QtGui.QLineEdit(self.frame)
        self.file_path_obj.setObjectName("file_path_obj")
        self.gridLayout_2.addWidget(self.file_path_obj, 5, 2, 1, 1)
        self.browse_btn_obj = QtGui.QPushButton(self.frame)
        self.browse_btn_obj.setObjectName("browse_btn_obj")
        self.gridLayout_2.addWidget(self.browse_btn_obj, 5, 3, 1, 1)
        self.sequence_comboBox_obj = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sequence_comboBox_obj.sizePolicy().hasHeightForWidth())
        self.sequence_comboBox_obj.setSizePolicy(sizePolicy)
        self.sequence_comboBox_obj.setObjectName("sequence_comboBox_obj")
        self.gridLayout_2.addWidget(self.sequence_comboBox_obj, 1, 2, 1, 2)
        self.scene_comboBox_obj = QtGui.QComboBox(self.frame)
        self.scene_comboBox_obj.setObjectName("scene_comboBox_obj")
        self.gridLayout_2.addWidget(self.scene_comboBox_obj, 2, 2, 1, 2)
        self.shot_comboBox_obj = QtGui.QComboBox(self.frame)
        self.shot_comboBox_obj.setObjectName("shot_comboBox_obj")
        self.gridLayout_2.addWidget(self.shot_comboBox_obj, 3, 2, 1, 2)
        self.version_comboBox_obj = QtGui.QComboBox(self.frame)
        self.version_comboBox_obj.setObjectName("version_comboBox_obj")
        self.gridLayout_2.addWidget(self.version_comboBox_obj, 4, 2, 1, 2)
        self.progress_obj = QtGui.QLabel(self.frame)
        self.progress_obj.setObjectName("progress_obj")
        self.gridLayout_2.addWidget(self.progress_obj, 7, 1, 1, 1)
        self.progress_bar_obj = QtGui.QProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_bar_obj.sizePolicy().hasHeightForWidth())
        self.progress_bar_obj.setSizePolicy(sizePolicy)
        self.progress_bar_obj.setProperty("value", 0)
        self.progress_bar_obj.setObjectName("progress_bar_obj")
        self.gridLayout_2.addWidget(self.progress_bar_obj, 7, 2, 1, 2)
        self.status_obj = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_obj.sizePolicy().hasHeightForWidth())
        self.status_obj.setSizePolicy(sizePolicy)
        self.status_obj.setObjectName("status_obj")
        self.gridLayout_2.addWidget(self.status_obj, 8, 1, 1, 1)
        self.line = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setBaseSize(QtCore.QSize(0, 6))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 6, 2, 1, 1)
        self.status_message_obj = QtGui.QPlainTextEdit(self.frame)
        self.status_message_obj.setEnabled(True)
        self.status_message_obj.setReadOnly(True)
        self.status_message_obj.setObjectName("status_message_obj")
        self.gridLayout_2.addWidget(self.status_message_obj, 8, 2, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.seq_obj.setBuddy(self.sequence_comboBox_obj)
        self.scn_obj.setBuddy(self.scene_comboBox_obj)
        self.shot_obj.setBuddy(self.shot_comboBox_obj)
        self.version_obj.setBuddy(self.version_comboBox_obj)

        self.retranslateUi(Form, **kwargs)
        QtCore.QObject.connect(self.sequence_comboBox_obj, QtCore.SIGNAL("currentIndexChanged(QString)"), self.get_scenes)
        QtCore.QObject.connect(self.scene_comboBox_obj, QtCore.SIGNAL("currentIndexChanged(QString)"), self.get_shots)
        QtCore.QObject.connect(self.shot_comboBox_obj, QtCore.SIGNAL("currentIndexChanged(QString)"), self.get_versions)
        QtCore.QObject.connect(self.browse_btn_obj, QtCore.SIGNAL("released()"), self.select_file)

        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.setTabOrder(self.sequence_comboBox_obj, self.scene_comboBox_obj)
        Form.setTabOrder(self.scene_comboBox_obj, self.shot_comboBox_obj)
        Form.setTabOrder(self.shot_comboBox_obj, self.version_comboBox_obj)
        Form.setTabOrder(self.version_comboBox_obj, self.file_path_obj)
        Form.setTabOrder(self.file_path_obj, self.browse_btn_obj)

        self.bootstrap()

    def bootstrap(self):
        self.scene = None
        self.shots = []
        self.versions = []

        #self.sequence_comboBox_obj.setEnabled(0)
        self.scene_comboBox_obj.setEnabled(0)
        self.shot_comboBox_obj.setEnabled(0)
        self.version_comboBox_obj.setEnabled(0)

        self.browse_btn_obj.setEnabled(1)
        self.file_path_obj.setEnabled(1)

        self.disqualify = True

        self.shot_comboBox_obj.addItem('<All>')
        self.version_comboBox_obj.addItem('<All>')

        if not self.__class__.ticket:
            self.tactic_login()

        if not self.__class__.sequences:
            self.get_seq_data()

        self.populate_seq_data()

    def retranslateUi(self, Form, **kwargs):
        self.item_count = kwargs.get('item_count')
        self.uuid4 = uuid.uuid4()

        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.input_obj.setText(QtGui.QApplication.translate("Form", "Input #{0}".format(self.item_count), None, QtGui.QApplication.UnicodeUTF8))
        self.seq_obj.setText(QtGui.QApplication.translate("Form", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.scn_obj.setText(QtGui.QApplication.translate("Form", "Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_obj.setText(QtGui.QApplication.translate("Form", "Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.version_obj.setText(QtGui.QApplication.translate("Form", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.path_obj.setText(QtGui.QApplication.translate("Form", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.browse_btn_obj.setText(QtGui.QApplication.translate("Form", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.progress_obj.setText(QtGui.QApplication.translate("Form", "Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.status_obj.setText(QtGui.QApplication.translate("Form", "Status", None, QtGui.QApplication.UnicodeUTF8))

    def select_file(self):
        file_path = str(QtGui.QFileDialog.getExistingDirectory(None, QtCore.QString("Open dir"), self.__class__.base_path, QtGui.QFileDialog.ShowDirsOnly|QtGui.QFileDialog.DontResolveSymlinks))
        if file_path.strip():
            self.file_path_obj.setText(file_path)


    def tactic_login(self):
        ip="tactic"
        proj="bilal"
        uname = "abhishek"
        passwd="abhishek"

        try:
            serverSetup.setupClientServer(server_name=ip, project_code=proj, login=uname, password=passwd)
            self.__class__.userQuery=qClass.queryClass(ip, proj)
            self.__class__.ticket=self.__class__.userQuery.userLogin(uname, passwd)
        except Exception, e:
            print >>sys.stderr, e.msg

    def get_seq_data(self):
        expr = "@SOBJECT(bilal/seq)"
        self.__class__.sequences = self.userQuery.server.eval(expr)

    def populate_seq_data(self):
        for seq in self.__class__.sequences:
            if seq:
                self.sequence_comboBox_obj.addItem(seq['name'])

    def get_scenes(self, seq):
        self.scene_comboBox_obj.clear()
        self.shot_comboBox_obj.clear()
        self.version_comboBox_obj.clear()

        seq = str(seq).encode('ascii')
        seq_code = self.userQuery.getSeqSObjectbyName(seq)
        if seq_code:
            sobjectSeq = seq_code[0]['code']
            filters=[]
            filters.append(("seq_code", sobjectSeq))

            scene=self.userQuery.server.query("bilal/scn", filters=filters)
            if scene:
                self.scene_comboBox_obj.setEnabled(1)

                self.scene = scene
                self.scene_comboBox_obj.addItem(scene[0]['name'])
            else:
                self.scene_comboBox_obj.setEnabled(0)
                self.shot_comboBox_obj.setEnabled(0)
                self.version_comboBox_obj.setEnabled(0)
                self.scene = ""
                self.shots = []
                self.versions = []
                #self.scene_comboBox_obj.addItem("<N/A>")

        self.status_message_obj.setPlainText("Scene Qualify?: " + str(not self.disqualify))

    def get_shots(self, scene):
        self.shot_comboBox_obj.clear()
        self.shots = ['<All>']

        seq = str(self.sequence_comboBox_obj.currentText()).encode('ascii')
        scene = str(scene).encode('ascii')

        sobjectSeq = self.userQuery.getSeqSObjectbyName(seq)
        if sobjectSeq:
            sobjectSeq = sobjectSeq[0]['code'].encode('ascii')
            sobjectScn = self.userQuery.getScnSObjectbyNameAndSeqCode(scene, sobjectSeq)
            if sobjectScn:
                sobjectShots = self.userQuery.getShtSObjectbyName(sobjectSeq, sobjectScn[0]['code'])
                if sobjectShots:
                    self.shots.extend(sobjectShots)
                    self.shot_comboBox_obj.setEnabled(1)
                    self.shot_comboBox_obj.addItem('<All>')
                    for shot in sobjectShots:
                        self.shot_comboBox_obj.addItem(shot['name'])
            else:
                self.shot_comboBox_obj.setEnabled(0)
                self.scene = ""
                self.shots = ['<All>']
                #self.shot_comboBox_obj.addItem('<N/A>')
        else:
            #ToDo
            self.shot_comboBox_obj.setEnabled(0)
            self.shots = ['<N/A>']
            #self.shot_comboBox_obj.addItem('<N/A>')

        self.status_message_obj.setPlainText("Shot Qualify?: " + str(not self.disqualify))

    def get_versions(self, shot):
        self.version_comboBox_obj.clear()
        self.versions = ['<Latest>', '<All>']

        seq = str(self.sequence_comboBox_obj.currentText()).encode('ascii')
        scn = str(self.scene_comboBox_obj.currentText()).encode('ascii')
        shot = str(self.shot_comboBox_obj.currentText()).encode('ascii')

        if shot not in self.versions:
            path = self.__class__.base_path + self.__class__.rel_exr_path
            #path = path.format("seq14", "scn28", "sh029")
            path = path.format(seq, scn, shot)
            print path

            paths = sorted(glob.glob(path))
            if paths:
                self.disqualify = False
                self.version_comboBox_obj.setEnabled(1)
                for path in paths:
                    ver = path.split("/")[-1]
                    self.versions.append(ver)
                    print ver
                for ver in self.versions:
                    self.version_comboBox_obj.addItem(ver)
            else:
                self.version_comboBox_obj.setEnabled(0)
                self.disqualify = True
        else:
            self.disqualify = False
            self.version_comboBox_obj.setEnabled(1)
            for ver in self.versions:
                self.version_comboBox_obj.addItem(ver)

        self.status_message_obj.setPlainText("Version Qualify?: " + str(not self.disqualify))



