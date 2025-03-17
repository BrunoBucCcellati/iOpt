from problems.Floudas import Floudas
from problems.GKLS import GKLS
from problems.Pern import Pern
from problems.Synthes import Synthes
from problems.Yuan import Yuan
from problems.ex1222 import ex1222
from problems.g2c import g2c
from problems.g8c import g8c
from problems.gbd import gbd
from problems.grishagin import Grishagin
from problems.grishagin_mco import Grishagin_mco
from problems.hill import Hill
from problems.mco_test1 import mco_test1
from problems.mco_test1_1 import mco_test1_1
from problems.mco_test3 import mco_test3
from problems.mco_test5 import mco_test5
from problems.mco_test6 import mco_test6
from problems.mco_test7 import mco_test7
from problems.nvs21 import nvs21
from problems.p1 import p1
from problems.p2 import p2
from problems.p7 import p7
from problems.rastrigin import Rastrigin
from problems.rastriginInt import RastriginInt
from problems.rastrigin_hidden_constraint import RastriginHiddenConstraint
from problems.rastrigin_int_hidden_constraint import RastriginIntHiddenConstraint
from problems.romeijn1c import Romeijn1c
from problems.romeijn2c import Romeijn2c
from problems.romeijn3c import Romeijn3c
from problems.romeijn5c import Romeijn5c
from problems.shekel import Shekel
from problems.shekel4 import Shekel4
from problems.stronginc2 import Stronginc2
from problems.stronginc3 import Stronginc3
from problems.stronginc5 import Stronginc5
from problems.xsquared import XSquared
from problems.test import test
from iOpt.solver import Solver
from iOpt.optimizer import optimizer
from iOpt.solver_parametrs import SolverParameters
from iOpt.output_system.listeners.static_painters import StaticPainterListener
from iOpt.output_system.listeners.static_painters import StaticPainterNDListener
from iOpt.output_system.listeners.static_painters import StaticDiscreteListener
from iOpt.output_system.listeners.animate_painters import AnimatePainterListener
from iOpt.output_system.listeners.animate_painters import AnimatePainterNDListener
from iOpt.output_system.listeners.console_outputers import ConsoleOutputListener
from examples.Genetic_algorithm.TSP._1D.Problems import ga_tsp_vary_mutation
from examples.Genetic_algorithm.TSP._2D.Problems import ga_tsp_2d
from examples.Machine_learning.NeuralNetwork.Segmentation.Problem.Cardio2D import Cardio2D
from examples.Machine_learning.SVC._1D.Problems import SVC_Fixed_Kernel
from examples.Machine_learning.SVC._1D.Problems import SVC_Fixed_Regularization
from examples.Machine_learning.SVC._2D.Problems import SVC_2d
from examples.Machine_learning.SVC._2D.Problems import MCO_SVC_2D_Transformators_State
from examples.Machine_learning.SVC._2D.Problems import SVC_2D_Float_Discrete
from examples.Machine_learning.SVC._2D.Problems.mco_breast_cancer import mco_breast_cancer
from examples.Machine_learning.SVC._3D.Problem import SVC_3D
from examples.Machine_learning.XGBoostRegression._2D.Problems.XGBR_2D_Gasturbine import XGBR_2d_Gasturbine
from examples.Machine_learning.XGBoostRegression._3D.Problems import XGB_3D
from iOpt.dashboard.static_dashboard import StaticDashboard


__all__ = [
    "Floudas",
    "GKLS",
    "Pern",
    "Synthes",
    "Yuan",
    "ex1222",
    "g2c",
    "g8c",
    "gbd",
    "Grishagin",
    "Grishagin_mco",
    "Hill",
    "mco_test1",
    "mco_test1_1",
    "mco_test3",
    "mco_test5",
    "mco_test6",
    "mco_test7",
    "nvs21",
    "p1",
    "p2",
    "p7",
    "Rastrigin",
    "RastriginInt",
    "RastriginHiddenConstraint",
    "RastriginIntHiddenConstraint",
    "Romeijn1c",
    "Romeijn2c",
    "Romeijn3c",
    "Romeijn5c",
    "Shekel",
    "Shekel4",
    "Stronginc2",
    "Stronginc3",
    "Stronginc5",
    "XSquared",
    "test",
    "ga_tsp_vary_mutation",
    "ga_tsp_2d",
    "Cardio2D",
    "SVC_Fixed_Kernel",
    "SVC_Fixed_Regularization",
    "SVC_2d",
    "MCO_SVC_2D_Transformators_State",
    "SVC_2D_Float_Discrete",
    "mco_breast_cancer",
    "SVC_3D",
    "XGBR_2d_Gasturbine",
    "XGB_3D",
    "StaticDashboard",
    "Solver",
    "optimizer",
    "SolverParameters",
    "StaticPainterListener",
    "StaticPainterNDListener",
    "StaticDiscreteListener",
    "AnimatePainterListener",
    "AnimatePainterNDListener",
    "ConsoleOutputListener",
]
