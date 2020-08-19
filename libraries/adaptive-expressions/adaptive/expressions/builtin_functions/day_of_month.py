from datetime import datetime
from ..expression_evaluator import ExpressionEvaluator, EvaluateExpressionDelegate
from ..expression_type import DAYOFMONTH
from ..function_utils import FunctionUtils
from ..return_type import ReturnType


class DayOfMonth(ExpressionEvaluator):
    def __init__(self):
        super().__init__(
            DAYOFMONTH,
            DayOfMonth.evaluator(),
            ReturnType.Number,
            FunctionUtils.validate_unary,
        )

    @staticmethod
    def evaluator() -> EvaluateExpressionDelegate:
        def anonymous_function(args: list):
            def anonymous_func(date_time: datetime):
                return date_time.day, None

            return FunctionUtils.normalize_to_date_time(args[0], anonymous_func)

        return FunctionUtils.apply_with_error(anonymous_function)
