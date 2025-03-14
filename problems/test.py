import numpy as np
from iOpt.trial import Point
from iOpt.trial import FunctionValue
from iOpt.trial import Trial
from iOpt.problem import Problem


class test(Problem):

    def __init__(self, function: FunctionValue):
        super().__init__()
        self.flag = False
        self.function = function
        self.point = Point(float_variables=np.ndarray(shape=(self.number_of_float_variables), dtype=np.double))
        self.index = -1

    def suggest_float(self, name : str, dawn : float, up : float):
        if self.point.float_variables.size == 0:
            self.dimension += 1
            self.number_of_float_variables += 1

            if (self.flag == False):
                self.number_of_objectives = 1
                self.float_variable_names = np.ndarray(shape=(self.number_of_float_variables), dtype=str)
                self.lower_bound_of_float_variables = np.ndarray(shape=(self.number_of_float_variables), dtype=np.double)
                self.upper_bound_of_float_variables = np.ndarray(shape=(self.number_of_float_variables), dtype=np.double)
                self.flag = True

            else : 
                self.float_variable_names = np.resize(self.float_variable_names, (self.number_of_float_variables))
                self.lower_bound_of_float_variables = np.resize(self.lower_bound_of_float_variables, (self.number_of_float_variables))
                self.upper_bound_of_float_variables = np.resize(self.upper_bound_of_float_variables, (self.number_of_float_variables))

            self.float_variable_names[self.number_of_float_variables - 1] = name
            self.lower_bound_of_float_variables[self.number_of_float_variables - 1] = dawn
            self.upper_bound_of_float_variables[self.number_of_float_variables - 1] = up
            return 1

        else:
            self.index += 1
            return self.point.float_variables[self.index % self.number_of_float_variables]
        

    def calculate(self, point: Point, function_value: FunctionValue) -> FunctionValue:
        self.point = point
        function_value.value = self.function(self)
        return function_value
