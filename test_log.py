# import logging

# class MyFormatter(logging.Formatter):
#     def format(self, record):
#         # record.prefix = []
#         record.prefix_msg = ""
#         extra_prefix = record.args and record.args.get("prefix") or []
#         base_prefix = hasattr(record, "base_prefix") and record.base_prefix or []
#         prefix = base_prefix + extra_prefix
#         if prefix:
#             prefix_str = ''.join([f'[{p}]' for p in prefix])
#             record.prefix_msg = f"{prefix_str} - "

#         return super().format(record)

# logger = logging.getLogger('test')
# ch = logging.StreamHandler()
# ch.setFormatter(MyFormatter('%(prefix_msg)s %(name)s - %(levelname)s - %(message)s'))
# logging.basicConfig( level=logging.INFO, handlers=[ch] )
# print(logger)
# logger.info("debug message", {"prefix": ['layer1', 'layer2']})
# logger.info("This is my sample log")
# logger.info("debug message", {"test": ['layer1', 'layer2']})
# logger.info("This is my sample log", {"hello": "World"})

# logger_2 = logging.LoggerAdapter(logger, extra={"base_prefix": ["bronze"]})

# logger_2.info("test prefix_msg no prefix")
# logger_2.info("test prefix_msg", {"prefix": ['abc']})
# d = {"abc": 123}
# a = [1,2,3]
# logger_2.info(f"asdad {d} {a}")

# logger_2.info('asdada', d)

# print(logger.level)
# logger_3 = logging.getLogger('test')
# print(logger_3.level)
# print(logger.level)
# try:
#     logger.info(f"try with something error {msg}")
# except Exception as e:
#     logger.exception(e)
# logger.info("pass")