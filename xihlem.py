import nose


class Boxes:

    # Returns integer, the minimum number of boxes needed to hold a given number of items
    @staticmethod
    def minimalNumberOfBoxes(products, availableLargeBoxes, availableSmallBoxes):
        large_size = 5
        import ipdb
        ipdb.set_trace()
        if products % large_size:
            large_boxes = products // large_size
            small_boxes = products % (large_size * availableLargeBoxes)
            if small_boxes > availableSmallBoxes:
                return -1
            large_boxes = (products - small_boxes) / large_size
            if large_boxes > availableLargeBoxes:
                return -1
            return small_boxes + large_boxes
        else:
            return products / large_size


# nose.tools.assert_equal(Boxes.minimalNumberOfBoxes(16, 2, 10), 8)
# nose.tools.assert_equal(Boxes.minimalNumberOfBoxes(0, 2, 10), 0)
# nose.tools.assert_equal(Boxes.minimalNumberOfBoxes(1, 2, 10), 1)
# nose.tools.assert_equal(Boxes.minimalNumberOfBoxes(2, 2, 10), 2)
# nose.tools.assert_equal(Boxes.minimalNumberOfBoxes(3, 2, 10), 3)
# nose.tools.assert_equal(Boxes.minimalNumberOfBoxes(4, 2, 10), 4)
# nose.tools.assert_equal(Boxes.minimalNumberOfBoxes(5, 2, 10), 1)
nose.tools.assert_equal(Boxes.minimalNumberOfBoxes(6, 2, 10), 2)
nose.tools.assert_equal(Boxes.minimalNumberOfBoxes(10, 2, 10), 2)
nose.tools.assert_equal(Boxes.minimalNumberOfBoxes(15, 2, 10), 7)
#
#
#
# import re
#
#
# class PasswordValidation:
#
#     @staticmethod
#     def strong_password(strong_password):
#         if len(strong_password) < 12:
#             return False
#         if "123" in strong_password:
#             return False
#         if not any(map(str.islower, strong_password)):
#             return False
#         if not any(map(str.isupper, strong_password)):
#             return False
#         if not any(map(str.isdigit, strong_password)):
#             return False
#         return True
#
#
# # nose.tools.assert_equal(PasswordValidation.strong_password("Strong1Password"), True)
# # nose.tools.assert_equal(PasswordValidation.strong_password("strong1password"), False)
# # nose.tools.assert_equal(PasswordValidation.strong_password("strong1passw"), False)
# # nose.tools.assert_equal(PasswordValidation.strong_password("strongpassw"), False)
# # nose.tools.assert_equal(PasswordValidation.strong_password("strongpasswORd1asdas"), True)
# # nose.tools.assert_equal(PasswordValidation.strong_password("strongpasswORdasd"), False)
# # nose.tools.assert_equal(PasswordValidation.strong_password("strongpasswORdasd123"), False)
# # nose.tools.assert_equal(PasswordValidation.strong_password("strongpasswORdasd124"), True)
#
#
# import xml.etree.ElementTree as ET
#
#
# class LogParser:
#
#     @staticmethod
#     def ids_by_message(xml, message):
#         root = ET.fromstring(xml)
#         values = []
#         for child in root:
#             for sub_child in child:
#                 if sub_child.text == message:
#                     values.append(int(child.attrib["id"]))
#         return values
#
#
# xml = """<?xml version="1.0" encoding="UTF-8"?>
# <log>
#     <entry id="1">
#         <message>Application started</message>
#     </entry>
#     <entry id="2">
#         <message>Application ended</message>
#     </entry>
# </log>"""
#
# nose.tools.assert_equal(LogParser.ids_by_message(xml, 'Application ended'), [2])
#
# xml = """<?xml version="1.0" encoding="UTF-8"?>
# <log>
#     <entry id="1">
#         <message>Application ended</message>
#     </entry>
#     <entry id="2">
#         <message>Application ended</message>
#     </entry>
# </log>"""
# nose.tools.assert_equal(LogParser.ids_by_message(xml, 'Application ended'), [1, 2])
#
#
# xml = """<?xml version="1.0" encoding="UTF-8"?>
# <log>
#     <entry id="1">
#         <message>Application started</message>
#     </entry>
#     <entry id="2">
#         <message>Application started</message>
#     </entry>
# </log>"""
# nose.tools.assert_equal(LogParser.ids_by_message(xml, 'Application ended'), [])
#
