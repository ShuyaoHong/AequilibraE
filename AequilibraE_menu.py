# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AequilibraE - www.aequilibrae.com
                                 A QGIS plugin
 AequilibraE and other tools for Transportation modelers
                              -------------------
        begin                : 2014-03-19
        copyright            : AequilibraE developers 2014
        Original Author: Pedro Camargo pedro@xl-optim.com
        Contributors: 
        Licence: See LICENSE.TXT
 ***************************************************************************/


"""
# Import the PyQt and QGIS libraries
from qgis.core import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# Import the code for the dialog
from parameters_dialog import ParameterDialog
from Network_preparation_dialog import TQ_NetPrepDialog
from adds_connectors_dialog import AEQ_AddConnectors
from create_graph_dialog import Graph_Creation_Dialog
#from calibrate_gravity_dialog import CalibrateGravityDialog
from show_shortest_path_dialog import ShortestPathDialog
#from Transportation_modeling_dialogs import *
from impedance_matrix_dialogs import ImpedanceMatrixDialog

#from Trip_distribution_dialogs import *
#from GIS_tools_dialogs import *
from simple_tag_dialog import SimpleTagDialog
import sys

sys.dont_write_bytecode = True
import os.path


class AequilibraE_menu:
    def __init__(self, iface):
        self.iface = iface
        self.AequilibraE_menu = None

    def AequilibraE_add_submenu(self, submenu):
        if self.AequilibraE_menu is not None:
            self.AequilibraE_menu.addMenu(submenu)
        else:
            self.iface.addPluginToMenu("&AequilibraE", submenu.menuAction())

    def initGui(self):

        # CREATING MASTER MENU HEAD
        self.AequilibraE_menu = QMenu(QCoreApplication.translate("AequilibraE", "AequilibraE"))
        self.iface.mainWindow().menuBar().insertMenu(self.iface.firstRightStandardMenu().menuAction(),
                                                     self.AequilibraE_menu)

        # ########################################################################
        # ################# NETWORK MANIPULATION SUB-MENU  #######################

        self.network_menu = QMenu(QCoreApplication.translate("AequilibraE", "&Network Manipulation"))
        self.AequilibraE_add_submenu(self.network_menu)

        # Network preparation
        icon = QIcon(os.path.dirname(__file__) + "/icons/icon_network.png")
        self.network_prep_action = QAction(icon, u"Network Preparation", self.iface.mainWindow())
        QObject.connect(self.network_prep_action, SIGNAL("triggered()"), self.run_net_prep)
        self.network_menu.addAction(self.network_prep_action)


        # Adding Connectors
        icon = QIcon(os.path.dirname(__file__) + "/icons/icon_network.png")
        self.add_connectors_action = QAction(icon, u"Adding Connectors", self.iface.mainWindow())
        QObject.connect(self.add_connectors_action, SIGNAL("triggered()"), self.run_add_connectors)
        self.network_menu.addAction(self.add_connectors_action)


        # # ########################################################################
        # # ##################  TRIP DISTRIBUTION SUB-MENU  ########################
        #
        # self.trip_distribution_menu = QMenu(QCoreApplication.translate("AequilibraE", "&Trip Distribution"))
        # self.AequilibraE_add_submenu(self.trip_distribution_menu)
        #
        # # gravity calibration
        # icon = QIcon(os.path.dirname(__file__) + "/icons/icon_calibrate_gravity.png")
        # self.calibrate_gravity_action = QAction(icon, u"Calibrate Gravity", self.iface.mainWindow())
        # QObject.connect(self.calibrate_gravity_action, SIGNAL("triggered()"), self.run_calibrate_gravity)
        # self.trip_distribution_menu.addAction(self.calibrate_gravity_action)
        #
        # # Trip Distribution
        # icon = QIcon(os.path.dirname(__file__) + "/icons/icon_distribution.png")
        # self.trip_distr_action = QAction(icon, u"Trip Distribution", self.iface.mainWindow())
        # QObject.connect(self.trip_distr_action, SIGNAL("triggered()"), self.run_trip_distr)
        # self.trip_distribution_menu.addAction(self.trip_distr_action)


        # ########################################################################
        # ###################  PATH COMPUTATION SUB-MENU   #######################

        self.assignment_menu = QMenu(QCoreApplication.translate("AequilibraE", "&Paths and assignment"))
        self.AequilibraE_add_submenu(self.assignment_menu)

        # MATRIX HOLDER
        # icon = QIcon(os.path.dirname(__file__) + "/icons/icon_matrices.png")
        #    self.matrix_holder_action = QAction(icon,u"Matrices holder", self.iface.mainWindow())
        #    QObject.connect(self.matrix_holder_action, SIGNAL("triggered()"),self.run_matrix_holder)
        #    self.assignment_menu.addAction(self.matrix_holder_action)

        # Graph generation
        icon = QIcon(os.path.dirname(__file__) + "/icons/icon_graph_creation.png")
        self.graph_creation_action = QAction(icon, u"Create the graph", self.iface.mainWindow())
        QObject.connect(self.graph_creation_action, SIGNAL("triggered()"), self.run_create_graph)
        self.assignment_menu.addAction(self.graph_creation_action)

        # Shortest path computation
        icon = QIcon(os.path.dirname(__file__) + "/icons/single_shortest_path.png")
        self.shortest_path_action = QAction(icon, u"Shortest path", self.iface.mainWindow())
        QObject.connect(self.shortest_path_action, SIGNAL("triggered()"), self.run_shortest_path)
        self.assignment_menu.addAction(self.shortest_path_action)


        # Distance matrix generation
        icon = QIcon(os.path.dirname(__file__) + "/icons/icon_dist_matrix.png")
        self.dist_matrix_action = QAction(icon, u"Impedance matrix", self.iface.mainWindow())
        QObject.connect(self.dist_matrix_action, SIGNAL("triggered()"), self.run_dist_matrix)
        self.assignment_menu.addAction(self.dist_matrix_action)

        # # Traffic Assignment
        # icon = QIcon(os.path.dirname(__file__) + "/icons/icon_assignment.png")
        # self.traffic_assignment_action = QAction(icon, u"Traffic Assignment", self.iface.mainWindow())
        # QObject.connect(self.traffic_assignment_action, SIGNAL("triggered()"), self.run_traffic_assig)
        # self.assignment_menu.addAction(self.traffic_assignment_action)
        # #########################################################################


        # ########################################################################
        # #################        GIS TOOLS SUB-MENU    #########################
        self.gis_tools_menu = QMenu(QCoreApplication.translate("AequilibraE", "&GIS tools"))
        self.AequilibraE_add_submenu(self.gis_tools_menu)

        # # Node to area aggregation
        # icon = QIcon(os.path.dirname(__file__) + "/icons/icon_node_to_area.png")
        # self.node_to_area_action = QAction(icon, u"Aggregation: Node to Area", self.iface.mainWindow())
        # QObject.connect(self.node_to_area_action, SIGNAL("triggered()"), self.run_node_to_area)
        # self.gis_tools_menu.addAction(self.node_to_area_action)

        # Simple TAG
        icon = QIcon(os.path.dirname(__file__) + "/icons/icon_simple_tag.png")
        self.simple_tag_action = QAction(icon, u"Simple TAG", self.iface.mainWindow())
        QObject.connect(self.simple_tag_action, SIGNAL("triggered()"), self.run_simple_tag)
        self.gis_tools_menu.addAction(self.simple_tag_action)

        # ########################################################################
        # #################          LOOSE STUFF         #########################

        # Change parameters
        icon = QIcon(os.path.dirname(__file__) + "/icons/icon_parameters.png")
        self.parameters_action = QAction(icon, u"Parameters", self.iface.mainWindow())
        QObject.connect(self.parameters_action, SIGNAL("triggered()"), self.run_change_parameters)
        self.AequilibraE_menu.addAction(self.parameters_action)


    #########################################################################

    def unload(self):
        if self.AequilibraE_menu != None:
            self.iface.mainWindow().menuBar().removeAction(self.AequilibraE_menu.menuAction())
        else:
            self.iface.removePluginMenu("&AequilibraE", self.network_menu.menuAction())
            self.iface.removePluginMenu("&AequilibraE", self.assignment_menu.menuAction())
            self.iface.removePluginMenu("&AequilibraE", self.trip_distribution_menu.menuAction())
            self.iface.removePluginMenu("&AequilibraE", self.gis_tools_menu.menuAction())

    # run method that calls the network preparation section of the code
    def run_change_parameters(self):
        dlg2 = ParameterDialog(self.iface)
        dlg2.show()
        dlg2.exec_()

    def run_net_prep(self):
        dlg2 = TQ_NetPrepDialog(self.iface)
        dlg2.show()
        dlg2.exec_()
        # If we wanted modal, we would eliminate the dlg2.show()

    def run_add_connectors(self):
        dlg2 = AEQ_AddConnectors(self.iface)
        dlg2.show()
        dlg2.exec_()

    def run_matrix_holder(self):
        dlg2 = TQ_Matrix_Holder_Dialog(self.iface)
        dlg2.show()
        dlg2.exec_()

    def run_calibrate_gravity(self):
        dlg2 = CalibrateGravityDialog(self.iface)
        dlg2.show()
        dlg2.exec_()

    def run_trip_distr(self):
        dlg2 = TQ_Trip_Dist_Dialog(self.iface)
        dlg2.show()
        dlg2.exec_()

    def run_create_graph(self):
        dlg2 = Graph_Creation_Dialog(self.iface)
        dlg2.show()
        dlg2.exec_()

    def run_shortest_path(self):
        dlg2 = ShortestPathDialog(self.iface)
        dlg2.show()
        dlg2.exec_()

    def run_dist_matrix(self):
        dlg2 = ImpedanceMatrixDialog(self.iface)
        dlg2.show()
        dlg2.exec_()

    def run_traffic_assig(self):
        # show the dialog
        dlg = Traffic_AssignmentDialog(self.iface)
        dlg2.show()
        dlg2.exec_()

    def run_node_to_area(self):
        dlg2 = node_to_area_class(self.iface)
        dlg2.show()
        dlg2.exec_()

    def run_simple_tag(self):
        dlg2 = SimpleTagDialog(self.iface)
        dlg2.show()
        dlg2.exec_()
