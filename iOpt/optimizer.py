from problems.test import test
from iOpt.solver import Solver
from iOpt.problem import Problem
from iOpt.solver_parametrs import SolverParameters
from iOpt.output_system.listeners.static_painters import StaticPainterNDListener
from iOpt.output_system.listeners.static_painters import StaticPainterListener
from iOpt.output_system.listeners.static_painters import StaticDiscreteListener
from iOpt.output_system.listeners.static_painters import StaticPainterParetoListener
from iOpt.output_system.listeners.animate_painters import AnimatePainterListener
from iOpt.output_system.listeners.animate_painters import AnimatePainterNDListener
from iOpt.output_system.listeners.console_outputers import ConsoleOutputListener


class optimizer:
    def __init__(self,
                 objective,
                 solver_parameters= SolverParameters(),
                 ):
        
        if type(objective) == Problem:
            self.problem == objective
        else:
            self.problem = test(objective)
            objective(self.problem)

        self.solver = Solver(self.problem, solver_parameters)
        
    """
    Valid values ​​for "type_of_painter": "none", "static", "animate", "both",
    Valid values ​​for "type_of_static": "StaticDiscrete", "StaticPainter", "StaticPainterND", "StaticPainterPareto",
    Valid values ​​for "type_of_animate": "AnimatePainter", "AnimatePainterND".
    """

    def optimize(self,
                 console_mode='full', iters=100,

                 type_of_painter= "none",

                 type_of_static= "StaticPainterND",
                 file_name="", path_for_saves="", painter_mode='lines layers',
                 calc='objective function',
                 # for StaticPainterND
                 vars_indxs=[0, 1],
                 # for StaticPainterPareto
                 criteria_indxs=[0, 1],
                 # for StaticPainter
                 indx=0, is_points_at_bottom=False,
                 # for StaticDiscrete
                 painter_type='lines layers', numpoints=150, mrkrs=3,

                 type_of_animate= "AnimatePainterND",
                 animate_file_name="", animate_path_for_saves="", to_paint_obj_func=True,
                 # for AnimatePainter
                 animate_is_points_at_bottom=False, 
                 # for AnimatePainterND
                 animate_vars_indxs=[0, 1]):
        
        if type_of_painter == "static" or type_of_painter == "both":

            if type_of_static == "StaticDiscrete":
                spl_disc = StaticDiscreteListener(file_name,
                                   path_for_saves,
                                   painter_mode,
                                   calc,painter_type, numpoints, mrkrs)
                self.solver.add_listener(spl_disc)

            if type_of_static == "StaticPainter":
                spl = StaticPainterListener(file_name,
                                   path_for_saves,
                                   indx,
                                   is_points_at_bottom,
                                   painter_mode)
                self.solver.add_listener(spl)

            if type_of_static == "StaticPainterND":
                spl_nd = StaticPainterNDListener(file_name,
                                   path_for_saves,
                                   vars_indxs,
                                   painter_mode,
                                   calc)
                self.solver.add_listener(spl_nd)

            if type_of_static == "StaticPainterPareto":
                spl_pareto = StaticPainterParetoListener(file_name,
                                   path_for_saves,
                                   criteria_indxs)
                self.solver.add_listener(spl_pareto)

        if type_of_painter == "animate" or type_of_painter == "both":

            if type_of_animate == "AnimatePainter":
                apl = AnimatePainterListener(animate_file_name,
                                             animate_path_for_saves,
                                             animate_is_points_at_bottom,
                                             to_paint_obj_func)
                self.solver.add_listener(apl)

            if type_of_animate == "AnimatePainterND":
                apl_nd = AnimatePainterNDListener(animate_file_name,
                                             animate_path_for_saves,
                                             animate_vars_indxs,
                                             to_paint_obj_func)
                self.solver.add_listener(apl_nd)

        cfol = ConsoleOutputListener(console_mode, iters)
        self.solver.add_listener(cfol)
        
        sol = self.solver.solve()
        return sol
