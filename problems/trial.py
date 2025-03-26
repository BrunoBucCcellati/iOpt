import numpy
from iOpt.trial import Point
from iOpt.trial import FunctionValue
from iOpt.problem import Problem

class trial(Problem):

    def __init__(self, function: FunctionValue):

        super().__init__()
        self.function = function
        self.isFirstFloatVariable = True
        self.isFirstDiscreteVariable = True
        self.isInit = True

    def suggest_float(self, name : object, dawn : float, up : float):

        if self.isInit == True:

            if type(name) != str:
                raise Exception("Please enter the variable name in the str format 'name'")  
            
            self.dimension += 1
            self.number_of_float_variables += 1

            if self.isFirstFloatVariable == True:
                self.number_of_objectives = 1
                self.float_variable_names = numpy.ndarray(shape=(self.number_of_float_variables), dtype=object)
                self.lower_bound_of_float_variables = numpy.ndarray(shape=(self.number_of_float_variables), dtype=numpy.double)
                self.upper_bound_of_float_variables = numpy.ndarray(shape=(self.number_of_float_variables), dtype=numpy.double)
                self.isFirstFloatVariable = False

            else:
                self.float_variable_names = numpy.resize(self.float_variable_names, (self.number_of_float_variables))
                self.lower_bound_of_float_variables = numpy.resize(self.lower_bound_of_float_variables, (self.number_of_float_variables))
                self.upper_bound_of_float_variables = numpy.resize(self.upper_bound_of_float_variables, (self.number_of_float_variables))

            self.float_variable_names[self.number_of_float_variables - 1] = name
            self.lower_bound_of_float_variables[self.number_of_float_variables - 1] = dawn  
            self.upper_bound_of_float_variables[self.number_of_float_variables - 1] = up
            return dawn

        else:
            index = numpy.where(self.float_variable_names == name)
            return self.point.float_variables[index[0][0]]
        
    def suggest_discrete(self, name : object, value : object):

        if self.isInit == True:
            
            if type(name) != str:
                raise Exception("Please enter the variable name in the str format 'name'")  

            if self.isFirstDiscreteVariable == True:

                self.number_of_objectives = 1
                self.dimension += 1
                self.number_of_discrete_variables += 1
                self.discrete_variable_names = numpy.ndarray(shape=(1), dtype=object)
                self.discrete_variable_names[0] = name

                if type(value) == numpy.ndarray:
                    if value.ndim > 1 or value.size < 1:
                        raise Exception("The set of values ​​must be a linear non-empty sequence")
                    self.discrete_variable_values = numpy.ndarray(shape=(1, value.size), dtype=type(value[0]))
                    for i in range (value.size):
                        self.discrete_variable_values[0][i] = value[i]
                
                if type(value) == list or type(value) == tuple:
                    if len(value) < 1:
                        raise Exception("The set of values ​​must be a linear non-empty sequence")
                    self.discrete_variable_values = numpy.ndarray(shape=(1, len(value)), dtype=type(value[0]))
                    for i in range (len(value)):
                        if isinstance(value[i], list) or isinstance(value[i], tuple):
                            raise Exception("The set of values ​​must be a linear non-empty sequence")
                        self.discrete_variable_values[0][i] = value[i]

                if type(value) != numpy.ndarray and type(value) != list and type(value) != tuple:
                    self.discrete_variable_values = numpy.ndarray(shape=(1, 1), dtype=type(value))
                    self.discrete_variable_values[0][0] = value

                self.isFirstDiscreteVariable = False

            else:

                same_name = numpy.where(self.discrete_variable_names == name)
                rows, cols = self.discrete_variable_values.shape

                if numpy.size(same_name) == 0:
                    self.dimension += 1
                    self.number_of_discrete_variables += 1
                    self.discrete_variable_names = numpy.resize(self.discrete_variable_names, (self.number_of_discrete_variables))
                    self.discrete_variable_names[self.number_of_discrete_variables - 1] = name

                    if type(value) == numpy.ndarray:
                        if value.ndim > 1 or value.size < 1:
                            raise Exception("The set of values ​​must be a linear non-empty sequence") 
                        
                        delta = value.size - cols
                        if delta < 0:
                            delta = 0
                        temp = numpy.full((rows + 1, cols + delta), type(value[0])(False))
                        temp[:rows, :cols] = self.discrete_variable_values
                        self.discrete_variable_values = temp 

                        for i in range (value.size):
                            self.discrete_variable_values[self.number_of_discrete_variables - 1][i] = value[i]
                
                    if type(value) == list or type(value) == tuple:
                        if len(value) < 1:
                            raise Exception("The set of values ​​must be a linear non-empty sequence")
                        
                        delta = len(value) - cols
                        if delta < 0:
                            delta = 0
                        temp = numpy.full((rows + 1, cols + delta), type(value[0])(False))
                        temp[:rows, :cols] = self.discrete_variable_values
                        self.discrete_variable_values = temp 

                        for i in range (len(value)):
                            if isinstance(value[i], list) or isinstance(value[i], tuple):
                                raise Exception("The set of values ​​must be a linear non-empty sequence")
                            self.discrete_variable_values[self.number_of_discrete_variables - 1][i] = value[i]
                    
                    if type(value) != numpy.ndarray and type(value) != list and type(value) != tuple:
                        temp = numpy.full((rows + 1, cols), type(value)(False))
                        temp[:rows, :cols] = self.discrete_variable_values
                        self.discrete_variable_values = temp 
                    
                        self.discrete_variable_values[self.number_of_discrete_variables - 1][0] = value
                    
                else:
                    i_index = numpy.where(self.discrete_variable_names == name)[0][0]
                    j_index = numpy.where(self.discrete_variable_values[i_index] == False)
                    if numpy.size(j_index) == 0:
                        
                        if type(value) == numpy.ndarray:
                            if value.ndim > 1 or value.size < 1:
                                raise Exception("The set of values ​​must be a linear non-empty sequence") 
                        
                            temp = numpy.full((rows, cols + value.size), type(value[0])(False))
                            temp[:rows, :cols] = self.discrete_variable_values
                            self.discrete_variable_values = temp 

                            for i in range (value.size):
                                self.discrete_variable_values[i_index][len(self.discrete_variable_values[0]) - value.size + i] = value[i]
                
                        if type(value) == list or type(value) == tuple:
                            if len(value) < 1:
                                raise Exception("The set of values ​​must be a linear non-empty sequence")
                        
                            temp = numpy.full((rows, cols + len(value)), type(value[0])(False))
                            temp[:rows, :cols] = self.discrete_variable_values
                            self.discrete_variable_values = temp 

                            for i in range (len(value)):
                                if isinstance(value[i], list) or isinstance(value[i], tuple):
                                    raise Exception("The set of values ​​must be a linear non-empty sequence")
                                self.discrete_variable_values[i_index][len(self.discrete_variable_values[0]) - len(value) + i] = value[i]
                    
                        if type(value) != numpy.ndarray and type(value) != list and type(value) != tuple:
                            temp = numpy.full((rows, cols + 1), type(value)(False))
                            temp[:rows, :cols] = self.discrete_variable_values
                            self.discrete_variable_values = temp

                            self.discrete_variable_values[i_index][len(self.discrete_variable_values[0]) - 1] = value
                    else:
                        
                        if type(value) == numpy.ndarray:
                            if value.ndim > 1 or value.size < 1:
                                raise Exception("The set of values ​​must be a linear non-empty sequence") 
                            
                            temp = numpy.full((rows, cols + value.size - j_index[0][0]), type(value[0])(False))
                            temp[:rows, :cols] = self.discrete_variable_values
                            self.discrete_variable_values = temp 

                            for i in range (value.size):
                                self.discrete_variable_values[i_index][j_index[0][0] + i] = value[i]
                
                        if type(value) == list or type(value) == tuple:
                            if len(value) < 1:
                                raise Exception("The set of values ​​must be a linear non-empty sequence")
                        
                            temp = numpy.full((rows, cols + len(value) - j_index[0][0]), type(value[0])(False))
                            temp[:rows, :cols] = self.discrete_variable_values
                            self.discrete_variable_values = temp 

                            for i in range (len(value)):
                                if isinstance(value[i], list) or isinstance(value[i], tuple):
                                    raise Exception("The set of values ​​must be a linear non-empty sequence")
                                self.discrete_variable_values[i_index][j_index[0][0] + i] = value[i]
                    
                        if type(value) != numpy.ndarray and type(value) != list and type(value) != tuple:
                            self.discrete_variable_values[i_index][j_index[0][0]] = value

            if type(value) == numpy.ndarray or type(value) == list or type(value) == tuple:
                return value[0]
            else:
                return value
        
        else:
            i_index = numpy.where(self.discrete_variable_names == name)[0][0]
            return self.point.discrete_variables[i_index]
        

    def calculate(self, point: Point, function_value: FunctionValue):
        self.point = point
        self.isInit = False
        function_value.value = self.function(self)
        return function_value
