# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mutant.ui'
#
# Created: Sat Aug 22 14:51:05 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Mutant(object):
    def setupUi(self, Mutant):
        Mutant.setObjectName(_fromUtf8("Mutant"))
        Mutant.resize(360, 393)
        self.gridLayout = QtGui.QGridLayout(Mutant)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(Mutant)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabTable = QtGui.QWidget()
        self.tabTable.setObjectName(_fromUtf8("tabTable"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabTable)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget = QtGui.QWidget(self.tabTable)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cbxDigits = QtGui.QCheckBox(self.widget)
        self.cbxDigits.setObjectName(_fromUtf8("cbxDigits"))
        self.horizontalLayout_3.addWidget(self.cbxDigits)
        self.spinDigits = QtGui.QSpinBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinDigits.sizePolicy().hasHeightForWidth())
        self.spinDigits.setSizePolicy(sizePolicy)
        self.spinDigits.setMaximum(99)
        self.spinDigits.setProperty("value", 2)
        self.spinDigits.setObjectName(_fromUtf8("spinDigits"))
        self.horizontalLayout_3.addWidget(self.spinDigits)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.exportPushButton = QtGui.QPushButton(self.widget)
        self.exportPushButton.setObjectName(_fromUtf8("exportPushButton"))
        self.horizontalLayout_3.addWidget(self.exportPushButton)
        self.verticalLayout_2.addWidget(self.widget)
        self.valueTable = QtGui.QTableWidget(self.tabTable)
        self.valueTable.setObjectName(_fromUtf8("valueTable"))
        self.valueTable.setColumnCount(5)
        self.valueTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.valueTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.valueTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.valueTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.valueTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.valueTable.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.valueTable)
        self.tabWidget.addTab(self.tabTable, _fromUtf8(""))
        self.tabGraph = QtGui.QWidget()
        self.tabGraph.setObjectName(_fromUtf8("tabGraph"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabGraph)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.graphControls = QtGui.QWidget(self.tabGraph)
        self.graphControls.setObjectName(_fromUtf8("graphControls"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.graphControls)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.enableStatistics = QtGui.QCheckBox(self.graphControls)
        self.enableStatistics.setObjectName(_fromUtf8("enableStatistics"))
        self.horizontalLayout_2.addWidget(self.enableStatistics)
        self.yAutoCheckBox = QtGui.QCheckBox(self.graphControls)
        self.yAutoCheckBox.setEnabled(True)
        self.yAutoCheckBox.setChecked(True)
        self.yAutoCheckBox.setObjectName(_fromUtf8("yAutoCheckBox"))
        self.horizontalLayout_2.addWidget(self.yAutoCheckBox)
        self.minYLabel = QtGui.QLabel(self.graphControls)
        self.minYLabel.setEnabled(True)
        self.minYLabel.setObjectName(_fromUtf8("minYLabel"))
        self.horizontalLayout_2.addWidget(self.minYLabel)
        self.leYMin = QtGui.QLineEdit(self.graphControls)
        self.leYMin.setEnabled(False)
        self.leYMin.setObjectName(_fromUtf8("leYMin"))
        self.horizontalLayout_2.addWidget(self.leYMin)
        self.maxYLabel = QtGui.QLabel(self.graphControls)
        self.maxYLabel.setEnabled(True)
        self.maxYLabel.setObjectName(_fromUtf8("maxYLabel"))
        self.horizontalLayout_2.addWidget(self.maxYLabel)
        self.leYMax = QtGui.QLineEdit(self.graphControls)
        self.leYMax.setEnabled(False)
        self.leYMax.setObjectName(_fromUtf8("leYMax"))
        self.horizontalLayout_2.addWidget(self.leYMax)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.graphControls, 0, 0, 1, 2)
        self.plotLibSelector = QtGui.QComboBox(self.tabGraph)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotLibSelector.sizePolicy().hasHeightForWidth())
        self.plotLibSelector.setSizePolicy(sizePolicy)
        self.plotLibSelector.setObjectName(_fromUtf8("plotLibSelector"))
        self.gridLayout_2.addWidget(self.plotLibSelector, 1, 0, 1, 1)
        self.exportPushButton_2 = QtGui.QPushButton(self.tabGraph)
        self.exportPushButton_2.setEnabled(False)
        self.exportPushButton_2.setCheckable(False)
        self.exportPushButton_2.setFlat(False)
        self.exportPushButton_2.setObjectName(_fromUtf8("exportPushButton_2"))
        self.gridLayout_2.addWidget(self.exportPushButton_2, 1, 1, 1, 1)
        self.toggleInterpolation = QtGui.QCheckBox(self.tabGraph)
        self.toggleInterpolation.setEnabled(False)
        self.toggleInterpolation.setObjectName(_fromUtf8("toggleInterpolation"))
        self.gridLayout_2.addWidget(self.toggleInterpolation, 2, 0, 1, 1)
        self.stackedWidget = QtGui.QStackedWidget(self.tabGraph)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.gridLayout_2.addWidget(self.stackedWidget, 3, 0, 1, 2)
        self.tabWidget.addTab(self.tabGraph, _fromUtf8(""))
        self.tabOptions = QtGui.QWidget()
        self.tabOptions.setObjectName(_fromUtf8("tabOptions"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabOptions)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.selectLayerGrid = QtGui.QGridLayout()
        self.selectLayerGrid.setObjectName(_fromUtf8("selectLayerGrid"))
        self.bandSelectionLabel = QtGui.QLabel(self.tabOptions)
        self.bandSelectionLabel.setObjectName(_fromUtf8("bandSelectionLabel"))
        self.selectLayerGrid.addWidget(self.bandSelectionLabel, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.selectLayerGrid.addItem(spacerItem2, 1, 2, 1, 1)
        self.layerSelectionLabel = QtGui.QLabel(self.tabOptions)
        self.layerSelectionLabel.setObjectName(_fromUtf8("layerSelectionLabel"))
        self.selectLayerGrid.addWidget(self.layerSelectionLabel, 1, 0, 1, 1)
        self.layerSelection = QtGui.QComboBox(self.tabOptions)
        self.layerSelection.setObjectName(_fromUtf8("layerSelection"))
        self.layerSelection.addItem(_fromUtf8(""))
        self.layerSelection.addItem(_fromUtf8(""))
        self.layerSelection.addItem(_fromUtf8(""))
        self.layerSelection.addItem(_fromUtf8(""))
        self.selectLayerGrid.addWidget(self.layerSelection, 1, 1, 1, 1)
        self.bandSelection = QtGui.QComboBox(self.tabOptions)
        self.bandSelection.setObjectName(_fromUtf8("bandSelection"))
        self.bandSelection.addItem(_fromUtf8(""))
        self.bandSelection.addItem(_fromUtf8(""))
        self.bandSelection.addItem(_fromUtf8(""))
        self.selectLayerGrid.addWidget(self.bandSelection, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.selectLayerGrid, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.tabOptions)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.plotOnMove = QtGui.QCheckBox(self.tabOptions)
        self.plotOnMove.setObjectName(_fromUtf8("plotOnMove"))
        self.gridLayout_3.addWidget(self.plotOnMove, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.tabOptions)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 1)
        self.setActiveLayerLabel = QtGui.QLabel(self.tabOptions)
        self.setActiveLayerLabel.setObjectName(_fromUtf8("setActiveLayerLabel"))
        self.gridLayout_3.addWidget(self.setActiveLayerLabel, 4, 0, 1, 1)
        self.selectStringGrid = QtGui.QGridLayout()
        self.selectStringGrid.setObjectName(_fromUtf8("selectStringGrid"))
        self.selectionStringLabel = QtGui.QLabel(self.tabOptions)
        self.selectionStringLabel.setObjectName(_fromUtf8("selectionStringLabel"))
        self.selectStringGrid.addWidget(self.selectionStringLabel, 0, 0, 1, 1)
        self.selectionStringLineEdit = QtGui.QLineEdit(self.tabOptions)
        self.selectionStringLineEdit.setEnabled(False)
        self.selectionStringLineEdit.setObjectName(_fromUtf8("selectionStringLineEdit"))
        self.selectStringGrid.addWidget(self.selectionStringLineEdit, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.selectStringGrid, 5, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.tabOptions)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_3.addWidget(self.line_3, 6, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.tabOptions)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 7, 0, 1, 1)
        self.selectionTable = QtGui.QTableWidget(self.tabOptions)
        self.selectionTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.selectionTable.setObjectName(_fromUtf8("selectionTable"))
        self.selectionTable.setColumnCount(4)
        self.selectionTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.selectionTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.selectionTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.selectionTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.selectionTable.setHorizontalHeaderItem(3, item)
        self.gridLayout_3.addWidget(self.selectionTable, 8, 0, 1, 1)
        self.tabWidget.addTab(self.tabOptions, _fromUtf8(""))
        self.tabMulti = QtGui.QWidget()
        self.tabMulti.setObjectName(_fromUtf8("tabMulti"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tabMulti)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.enableMTAnalysesCheckBox = QtGui.QCheckBox(self.tabMulti)
        self.enableMTAnalysesCheckBox.setObjectName(_fromUtf8("enableMTAnalysesCheckBox"))
        self.gridLayout_4.addWidget(self.enableMTAnalysesCheckBox, 0, 0, 1, 2)
        self.priorityLabel = QtGui.QLabel(self.tabMulti)
        self.priorityLabel.setEnabled(False)
        self.priorityLabel.setObjectName(_fromUtf8("priorityLabel"))
        self.gridLayout_4.addWidget(self.priorityLabel, 1, 0, 1, 3)
        self.extractionPriorityListWidget = QtGui.QListWidget(self.tabMulti)
        self.extractionPriorityListWidget.setEnabled(False)
        self.extractionPriorityListWidget.setToolTip(_fromUtf8(""))
        self.extractionPriorityListWidget.setWhatsThis(_fromUtf8(""))
        self.extractionPriorityListWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.extractionPriorityListWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.extractionPriorityListWidget.setObjectName(_fromUtf8("extractionPriorityListWidget"))
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.extractionPriorityListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.extractionPriorityListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.extractionPriorityListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.extractionPriorityListWidget.addItem(item)
        self.gridLayout_4.addWidget(self.extractionPriorityListWidget, 2, 0, 1, 3)
        self.cutFirst = QtGui.QSpinBox(self.tabMulti)
        self.cutFirst.setMaximum(999)
        self.cutFirst.setObjectName(_fromUtf8("cutFirst"))
        self.gridLayout_4.addWidget(self.cutFirst, 3, 0, 1, 2)
        self.dateLength = QtGui.QSpinBox(self.tabMulti)
        self.dateLength.setMaximum(999)
        self.dateLength.setProperty("value", 0)
        self.dateLength.setObjectName(_fromUtf8("dateLength"))
        self.gridLayout_4.addWidget(self.dateLength, 4, 0, 1, 2)
        self.sampleLabel = QtGui.QLabel(self.tabMulti)
        self.sampleLabel.setObjectName(_fromUtf8("sampleLabel"))
        self.gridLayout_4.addWidget(self.sampleLabel, 5, 0, 1, 1)
        self.sampleLineEdit = QtGui.QLineEdit(self.tabMulti)
        self.sampleLineEdit.setReadOnly(True)
        self.sampleLineEdit.setObjectName(_fromUtf8("sampleLineEdit"))
        self.gridLayout_4.addWidget(self.sampleLineEdit, 5, 1, 1, 2)
        self.patternLabel = QtGui.QLabel(self.tabMulti)
        self.patternLabel.setEnabled(False)
        self.patternLabel.setObjectName(_fromUtf8("patternLabel"))
        self.gridLayout_4.addWidget(self.patternLabel, 6, 0, 1, 1)
        self.patternLineEdit = QtGui.QLineEdit(self.tabMulti)
        self.patternLineEdit.setEnabled(False)
        self.patternLineEdit.setObjectName(_fromUtf8("patternLineEdit"))
        self.gridLayout_4.addWidget(self.patternLineEdit, 6, 1, 1, 2)
        self.writeMetaDataCheckBox = QtGui.QCheckBox(self.tabMulti)
        self.writeMetaDataCheckBox.setEnabled(False)
        self.writeMetaDataCheckBox.setChecked(True)
        self.writeMetaDataCheckBox.setTristate(False)
        self.writeMetaDataCheckBox.setObjectName(_fromUtf8("writeMetaDataCheckBox"))
        self.gridLayout_4.addWidget(self.writeMetaDataCheckBox, 7, 0, 1, 2)
        self.writeMetaPushButton = QtGui.QPushButton(self.tabMulti)
        self.writeMetaPushButton.setObjectName(_fromUtf8("writeMetaPushButton"))
        self.gridLayout_4.addWidget(self.writeMetaPushButton, 7, 2, 1, 1)
        self.tabWidget.addTab(self.tabMulti, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.toggleFilter = QtGui.QCheckBox(self.tab)
        self.toggleFilter.setEnabled(False)
        self.toggleFilter.setGeometry(QtCore.QRect(10, 10, 126, 21))
        self.toggleFilter.setObjectName(_fromUtf8("toggleFilter"))
        self.toggleMutant = QtGui.QCheckBox(self.tab)
        self.toggleMutant.setGeometry(QtCore.QRect(20, 50, 72, 21))
        self.toggleMutant.setObjectName(_fromUtf8("toggleMutant"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        self.labelStatus = QtGui.QLabel(Mutant)
        self.labelStatus.setText(_fromUtf8(""))
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.gridLayout.addWidget(self.labelStatus, 1, 0, 1, 1)

        self.retranslateUi(Mutant)
        self.tabWidget.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QObject.connect(self.toggleMutant, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.toggleFilter.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Mutant)

    def retranslateUi(self, Mutant):
        Mutant.setWindowTitle(_translate("Mutant", "Form", None))
        self.cbxDigits.setToolTip(_translate("Mutant", "Specify how many decimals to show in table", None))
        self.cbxDigits.setText(_translate("Mutant", "Decimals", None))
        self.exportPushButton.setToolTip(_translate("Mutant", "Export values from table to CSV", None))
        self.exportPushButton.setText(_translate("Mutant", "Export to CSV", None))
        self.valueTable.setSortingEnabled(True)
        item = self.valueTable.horizontalHeaderItem(0)
        item.setText(_translate("Mutant", "Layer", None))
        item = self.valueTable.horizontalHeaderItem(1)
        item.setText(_translate("Mutant", "Value", None))
        item = self.valueTable.horizontalHeaderItem(2)
        item.setText(_translate("Mutant", "Date", None))
        item = self.valueTable.horizontalHeaderItem(3)
        item.setText(_translate("Mutant", "X Coordinate", None))
        item = self.valueTable.horizontalHeaderItem(4)
        item.setText(_translate("Mutant", "Y Coordinate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTable), _translate("Mutant", "Table", None))
        self.enableStatistics.setToolTip(_translate("Mutant", "Compute min/max when layers are loaded", None))
        self.enableStatistics.setText(_translate("Mutant", "Stats", None))
        self.yAutoCheckBox.setToolTip(_translate("Mutant", "Autozoom to min and max of all loaded values", None))
        self.yAutoCheckBox.setText(_translate("Mutant", "Auto", None))
        self.minYLabel.setText(_translate("Mutant", "Y min", None))
        self.maxYLabel.setText(_translate("Mutant", "Y max", None))
        self.plotLibSelector.setToolTip(_translate("Mutant", "Select plotting toolkit\n"
"Qwt toolkit (faster but soon unmaintained)\n"
"matplotlib (slower but maintained)\n"
"PyQtGraph (fast but lacking some features)", None))
        self.exportPushButton_2.setToolTip(_translate("Mutant", "Export values from table to CSV", None))
        self.exportPushButton_2.setText(_translate("Mutant", "Export to CSV", None))
        self.toggleInterpolation.setText(_translate("Mutant", "Draw full line", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGraph), _translate("Mutant", "Graph", None))
        self.bandSelectionLabel.setText(_translate("Mutant", "Show bands:", None))
        self.layerSelectionLabel.setText(_translate("Mutant", "Show layers:", None))
        self.layerSelection.setItemText(0, _translate("Mutant", "Visible layers", None))
        self.layerSelection.setItemText(1, _translate("Mutant", "All layers", None))
        self.layerSelection.setItemText(2, _translate("Mutant", "Manual selection", None))
        self.layerSelection.setItemText(3, _translate("Mutant", "By selection string", None))
        self.bandSelection.setItemText(0, _translate("Mutant", "All bands", None))
        self.bandSelection.setItemText(1, _translate("Mutant", "Active bands", None))
        self.bandSelection.setItemText(2, _translate("Mutant", "Selected bands", None))
        self.plotOnMove.setToolTip(_translate("Mutant", "Replaces active map tool. Use this to select a particular point or if plotting is slow (e.g. when using mpl Graph).", None))
        self.plotOnMove.setText(_translate("Mutant", "Plot values only when mouse is clicked", None))
        self.setActiveLayerLabel.setText(_translate("Mutant", "Select layers by selection string:", None))
        self.selectionStringLabel.setToolTip(_translate("Mutant", "<html><head/><body>\n"
"<table border=\"0\">\n"
"<tr><td>*</td><td> matches everything</td></tr>\n"
"<tr><td>?</td><td> matches any single character</td></tr>\n"
"<tr><td>[seq]</td><td> matches any character in seq</td></tr>\n"
"<tr><td>[!seq]</td><td> matches any character not in seq</td></tr>\n"
"</table></body></html>", None))
        self.selectionStringLabel.setText(_translate("Mutant", "Selection string:", None))
        self.selectionStringLineEdit.setToolTip(_translate("Mutant", "<html><head/><body>\n"
"<table border=\"0\">\n"
"<tr><td>*</td><td> matches everything</td></tr>\n"
"<tr><td>?</td><td> matches any single character</td></tr>\n"
"<tr><td>[seq]</td><td> matches any character in seq</td></tr>\n"
"<tr><td>[!seq]</td><td> matches any character not in seq</td></tr>\n"
"</table></body></html>", None))
        self.selectionStringLineEdit.setText(_translate("Mutant", "*1?[89][!5-8]*", None))
        self.label_5.setText(_translate("Mutant", "Select active layers and display options:", None))
        item = self.selectionTable.horizontalHeaderItem(0)
        item.setToolTip(_translate("Mutant", "Select layers", None))
        item = self.selectionTable.horizontalHeaderItem(1)
        item.setText(_translate("Mutant", "Layer", None))
        item = self.selectionTable.horizontalHeaderItem(2)
        item.setText(_translate("Mutant", "#", None))
        item.setToolTip(_translate("Mutant", "Select bands", None))
        item = self.selectionTable.horizontalHeaderItem(3)
        item.setText(_translate("Mutant", "Bands", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOptions), _translate("Mutant", "Options", None))
        self.enableMTAnalysesCheckBox.setToolTip(_translate("Mutant", "<html><head/><body><p>Data will be reordered chronologically and points with no data will be omitted in the graph.</p></body></html>", None))
        self.enableMTAnalysesCheckBox.setText(_translate("Mutant", "Enable multi-temporal analysis", None))
        self.priorityLabel.setText(_translate("Mutant", "Extract time from (highest priority on top):\n"
"Drag & Drop Fields", None))
        __sortingEnabled = self.extractionPriorityListWidget.isSortingEnabled()
        self.extractionPriorityListWidget.setSortingEnabled(False)
        item = self.extractionPriorityListWidget.item(0)
        item.setText(_translate("Mutant", "XML", None))
        item = self.extractionPriorityListWidget.item(1)
        item.setText(_translate("Mutant", "Filename", None))
        item = self.extractionPriorityListWidget.item(2)
        item.setText(_translate("Mutant", "Exif", None))
        item = self.extractionPriorityListWidget.item(3)
        item.setText(_translate("Mutant", "TIFF-Header", None))
        self.extractionPriorityListWidget.setSortingEnabled(__sortingEnabled)
        self.cutFirst.setSuffix(_translate("Mutant", " characters", None))
        self.cutFirst.setPrefix(_translate("Mutant", "Cut first ", None))
        self.dateLength.setSuffix(_translate("Mutant", " characters long", None))
        self.dateLength.setPrefix(_translate("Mutant", "Datestring is ", None))
        self.sampleLabel.setText(_translate("Mutant", "Sample", None))
        self.patternLabel.setText(_translate("Mutant", "Datepattern:", None))
        self.patternLineEdit.setText(_translate("Mutant", "%Y%j%H%M%S", None))
        self.writeMetaDataCheckBox.setText(_translate("Mutant", "Write time to metadata (XML)", None))
        self.writeMetaPushButton.setText(_translate("Mutant", "Write Meta", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMulti), _translate("Mutant", "Time", None))
        self.toggleFilter.setToolTip(_translate("Mutant", "proof of concept - to be extended", None))
        self.toggleFilter.setText(_translate("Mutant", "Enable Filtering", None))
        self.toggleMutant.setToolTip(_translate("Mutant", "Can also be enabled using the toolbar icon", None))
        self.toggleMutant.setText(_translate("Mutant", "Enable", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Mutant", "Filtering", None))

