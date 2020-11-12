from utils import loggerutils


class ReportLogMain:
    """
    Wrapper class includes the patterns used for start and end test suite, steps and cases methods
    Also, includes log_info, log_error and log_critical methods for adding customised messages

    Class reads loggerutils file on the backend
    """

    def __init__(context):
        loggerutils.setup_logging()
        loggerutils.setup_formatted_logging(context)

    @staticmethod
    def log_info(context, message):
        context.logger.info(message)

    @staticmethod
    def log_error(context, message):
        context.logger.error(message, exc_info=True)

    def log_critical(context, message):
        context.logger.critical(message)

    @staticmethod
    def start_suite(context):
        context.logger.info("=================================")
        context.logger.info("Start Test Suite".upper())
        context.logger.info("=================================")

    @staticmethod
    def end_suite(context):
        context.logger.info("---------------------------------")
        context.logger.info("End Test Suite".upper())
        context.logger.info("---------------------------------")

    @staticmethod
    def start_test_case(context):
        context.logger.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        context.logger.info("Start Test Case           ")
        context.logger.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    @staticmethod
    def start_test_step(context, message):
        context.logger.info("---------------------------------")
        context.logger.info("Test Step - ".upper() + str(message).upper())
        context.logger.info("---------------------------------")

    @staticmethod
    def end_test_case(context):
        context.logger.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        context.logger.info("END - TEST CASE                 ")
        context.logger.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    @staticmethod
    def end_test_step(context):
        context.logger.info("---------------------------------")
        context.logger.info("END - TEST STEP          ")
        context.logger.info("---------------------------------")
