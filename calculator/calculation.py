'''CALCULATIONS'''
class Calculation:
    '''Represents a mathematical calculation with two operands and an operation.'''
    def __init__(self, first_operand,second_operand, operation):
        '''Initializes the calculation with two operands and an operation function.'''
        self.first_operand = first_operand
        self.second_operand = second_operand
        self.operation = operation  # Store the operation function
    def get_result(self):
        '''Returns the result of applying the stored operation to the operands.'''
        # Call the stored operation with a and b
        return self.operation(self.first_operand, self.second_operand)
