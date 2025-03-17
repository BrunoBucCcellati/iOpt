import numpy as np
from iOpt.trial import Point
from iOpt.trial import FunctionValue
from iOpt.trial import Trial
from iOpt.problem import Problem


class test(Problem):

    def __init__(self, function: FunctionValue):
        super().__init__()
        self.function = function
        self.isFirstFloatVariable = True
        self.isFirstDiscreteVariable = True
        self.isInit = True

    def suggest_float(self, name : object, dawn : float, up : float):
        if self.isInit == True:
            self.dimension += 1
            self.number_of_float_variables += 1

            if (self.isFirstFloatVariable == True):
                self.number_of_objectives = 1
                self.float_variable_names = np.ndarray(shape=(self.number_of_float_variables), dtype=object)
                self.lower_bound_of_float_variables = np.ndarray(shape=(self.number_of_float_variables), dtype=np.double)
                self.upper_bound_of_float_variables = np.ndarray(shape=(self.number_of_float_variables), dtype=np.double)
                self.isFirstFloatVariable = False

            else:
                self.float_variable_names = np.resize(self.float_variable_names, (self.number_of_float_variables))
                self.lower_bound_of_float_variables = np.resize(self.lower_bound_of_float_variables, (self.number_of_float_variables))
                self.upper_bound_of_float_variables = np.resize(self.upper_bound_of_float_variables, (self.number_of_float_variables))

            self.float_variable_names[self.number_of_float_variables - 1] = name
            self.lower_bound_of_float_variables[self.number_of_float_variables - 1] = dawn  
            self.upper_bound_of_float_variables[self.number_of_float_variables - 1] = up
            return dawn

        else:
            index = np.where(self.float_variable_names == name)
            return self.point.float_variables[index[0][0]]
        
    def suggest_int(self, name : object, value : object):
        if self.isInit == True:
            if (self.isFirstDiscreteVariable == True):
                self.dimension += 1
                self.number_of_discrete_variables += 1
                self.number_of_objectives = 1

                self.discrete_variable_names = np.ndarray(shape=(1), dtype=object)
                self.discrete_variable_values = np.ndarray(shape=(1, 1), dtype=object)

                self.discrete_variable_names[self.number_of_discrete_variables - 1] = name
                self.discrete_variable_values[self.number_of_discrete_variables - 1][0] = value

                self.isFirstDiscreteVariable = False

            else:
                same_name = np.where(self.discrete_variable_names == name)
                if np.size(same_name) == 0:
                    self.dimension += 1
                    self.number_of_discrete_variables += 1

                    rows, cols = self.discrete_variable_values.shape
                    temp = np.zeros((rows + 1, cols), dtype=np.int32)
                    temp[:rows, :cols] = self.discrete_variable_values
                    self.discrete_variable_values = temp

                    self.discrete_variable_names = np.resize(self.discrete_variable_names, (self.number_of_discrete_variables))

                    self.discrete_variable_names[self.number_of_discrete_variables - 1] = name
                    self.discrete_variable_values[self.number_of_discrete_variables - 1][0] = value
                    
                else:
                    index = np.where(self.discrete_variable_names == name)[0][0]
                    if type(self.discrete_variable_values[index][len(self.discrete_variable_values[index]) - 1]) == np.int32:
                        self.discrete_variable_values[index][len(self.discrete_variable_values[0]) - 1] = value
                            
                    else:
                        rows, cols = self.discrete_variable_values.shape
                        temp = np.zeros((rows, cols + 1), dtype=np.int32)
                        temp[:rows, :cols] = self.discrete_variable_values
                        self.discrete_variable_values = temp

                        self.discrete_variable_values[index][len(self.discrete_variable_values[0]) - 1] = value
            
            return value

        else:
            index = np.where(self.discrete_variable_names == name)[0][0]
            return int(self.point.discrete_variables[index])
        

    def calculate(self, point: Point, function_value: FunctionValue) -> FunctionValue:
        self.point = point
        self.isInit = False
        function_value.value = self.function(self)
        return function_value
