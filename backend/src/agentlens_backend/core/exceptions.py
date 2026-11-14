
class AgentLensException(Exception):
    pass

class DatasetNotFoundError(AgentLensException):
    pass

class EvaluationNotFoundError(AgentLensException):
    pass

class EvaluationExecutionError(AgentLensException):
    pass

