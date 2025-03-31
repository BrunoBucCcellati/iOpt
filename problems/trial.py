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
        self.num_of_objective_launches = 0

    def suggest_float(self, name : object, dawn : float, up : float):

        same_name = numpy.where(self.float_variable_names == name)
        if self.isInit == True or numpy.size(same_name) == 0:

            if type(name) != str:
                raise Exception("Please enter the variable name in the str format 'name'")  
            
            if up != float(up) or dawn != float(dawn):
                raise Exception("Range bounds must be representable as floating point numbers")
            
            if numpy.size(same_name) != 0:
                raise Exception("Floating point variable {} already added to task".format(name))
            
            self.dimension += 1
            self.number_of_float_variables += 1

            if self.isFirstFloatVariable == True:
                self.number_of_objectives = 1
                self.float_variable_names = numpy.ndarray(shape=(1), dtype=object)
                self.lower_bound_of_float_variables = numpy.ndarray(shape=(1), dtype=float)
                self.upper_bound_of_float_variables = numpy.ndarray(shape=(1), dtype=float)
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
            if self.num_of_objective_launches != 0:
                return dawn
            return self.point.float_variables[same_name[0][0]]
        
    def suggest_int(self, name : object, dawn : int, up : int, *, step : int = 1):

        same_name = numpy.where(self.discrete_variable_names == name)
        if self.isInit == True or numpy.size(same_name) == 0:

            if type(name) != str:
                raise Exception("Please enter the variable name in the str format 'name'")
            
            if type(up) != int or type(dawn) != int or type(step) != int:
                raise Exception("Range limits and step must be integers")
            
            if step > up - dawn:
                raise Exception("The maximum allowed step is the length of the range")
            
            if numpy.size(same_name) == 0:

                self.dimension += 1
                self.number_of_discrete_variables += 1
                
                if self.isFirstDiscreteVariable == True:
                    self.number_of_objectives = 1
                    self.discrete_variable_names = numpy.ndarray(shape=(1), dtype=object)
                    self.isFirstDiscreteVariable = False

                else:
                    self.discrete_variable_names = numpy.resize(self.discrete_variable_names, (self.number_of_discrete_variables))
                
                temp_list = []
                for i in range((up - dawn + 1) // step):
                    temp_list.append(dawn + i * step)
                self.discrete_variable_values.append(temp_list)
                self.discrete_variable_names[self.number_of_discrete_variables - 1] = name

            else:
                for i in range((up - dawn + 1) // step):
                    self.discrete_variable_values[same_name[0][0]].append(dawn + i * step)

            return dawn

        else:
            if self.num_of_objective_launches != 0:
                return dawn
            return self.point.discrete_variables[same_name[0][0]]
        
    def suggest_discrete(self, name : object, value : object):

        same_name = numpy.where(self.discrete_variable_names == name)
        if self.isInit == True or numpy.size(same_name) == 0:

            if type(name) != str:
                raise Exception("Please enter the variable name in the str format 'name'")
            
            if (not isinstance(value, (numpy.ndarray, list, tuple)) or not isinstance(value[0], (bool, int, str, float))) and not isinstance(value, (bool, int, str, float)):
                raise Exception("The set of values ​​of a discrete parameter is specified either by a linear non-empty sequence of bool, "
                    "int, float and str or by adding values ​​of the same types but contains {} which is of type "
                    "{}.".format(name, type(value)))
            
            if type(value) == numpy.ndarray:
                if value.ndim > 1:
                    raise Exception("The set of values ​​must be a linear sequence")         
            
            if numpy.size(same_name) == 0:

                self.dimension += 1
                self.number_of_discrete_variables += 1
                
                if self.isFirstDiscreteVariable == True:
                    self.number_of_objectives = 1
                    self.discrete_variable_names = numpy.ndarray(shape=(1), dtype=object)
                    self.isFirstDiscreteVariable = False

                else:
                    self.discrete_variable_names = numpy.resize(self.discrete_variable_names, (self.number_of_discrete_variables))
                
                temp_list = []

                if type(value) == numpy.ndarray:
                    for i in range (value.size):
                        temp_list.append(value[i])

                if type(value) == list or type(value) == tuple:
                    for i in range (len(value)):
                        temp_list.append(value[i])

                if type(value) != numpy.ndarray and type(value) != list and type(value) != tuple:
                    temp_list.append(value)

                self.discrete_variable_values.append(temp_list)
                self.discrete_variable_names[self.number_of_discrete_variables - 1] = name

            else:
                if type(value) == numpy.ndarray:
                    for i in range (value.size):
                        self.discrete_variable_values[same_name[0][0]].append(value[i])

                if type(value) == list or type(value) == tuple:
                    for i in range (len(value)):
                        self.discrete_variable_values[same_name[0][0]].append(value[i])

                if type(value) != numpy.ndarray and type(value) != list and type(value) != tuple:
                    self.discrete_variable_values[same_name[0][0]].append(value)

            if type(value) == numpy.ndarray:
                if value.size - 1 > self.num_of_objective_launches:
                    self.num_of_objective_launches = value.size - 1
                return value[0]
            if type(value) == list or type(value) == tuple:
                if len(value) - 1 > self.num_of_objective_launches:
                    self.num_of_objective_launches = len(value) - 1
                return value[0]
            else:
                return value
        
        else:
            if self.num_of_objective_launches != 0:
                if len(self.discrete_variable_values[same_name[0][0]]) > self.num_of_objective_launches:
                    return self.discrete_variable_values[same_name[0][0]][self.num_of_objective_launches]
                else:
                    return self.discrete_variable_values[same_name[0][0]][0]
            return self.point.discrete_variables[same_name[0][0]]
        
    def calculate(self, point: Point, function_value: FunctionValue):
        self.point = point
        function_value.value = self.function(self)
        return function_value
