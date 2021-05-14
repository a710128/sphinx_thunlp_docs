===============
Charts
===============

本篇主要介绍了如何在 **reST** 中插入图表。

表格
=================

在 **reST** 中，表格的表示方法是多种多样的，在这里我们会列出集中主流的表示方法。


字符画
------------------
这种表示方法是不太建议的，因为在表格中包含宽字符时会有对齐的问题。


.. code-block:: rst

    +------------------------+------------+----------+----------+
    | 第一行                 | Header 2   | Header 3 | Header 4 |
    | （第二行）             |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | ...        | ...      |          |
    +------------------------+------------+----------+----------+

**效果**

.. topic:: list
    :class: style-demo

    +------------------------+------------+----------+----------+
    | 第一行                 | Header 2   | Header 3 | Header 4 |
    | （第二行）             |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | ...        | ...      |          |
    +------------------------+------------+----------+----------+


简单表格
-----------------

.. code-block:: rst

    =====  =====  =======
    A      B      A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

**效果**

.. topic:: list
    :class: style-demo

    =====  =====  =======
    A      B      A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

列表表格
------------------

.. code-block:: rst

    .. list-table:: Title
        :widths: 25 25 50
        :header-rows: 1

        * - Heading row 1, column 1
          - Heading row 1, column 2
          - Heading row 1, column 3
        * - Row 1, column 1
          -
          - Row 1, column 3
        * - Row 2, column 1
          - Row 2, column 2
          - Row 2, column 3


**效果**

.. topic:: list
    :class: style-demo

    .. list-table:: Title
        :widths: 25 25 50
        :header-rows: 1

        * - Heading row 1, column 1
          - Heading row 1, column 2
          - Heading row 1, column 3
        * - Row 1, column 1
          -
          - Row 1, column 3
        * - Row 2, column 1
          - Row 2, column 2
          - Row 2, column 3


csv 表格
-----------------

文件链接： :download:`demo.csv <demo.csv>`

.. code-block:: rst

    .. csv-table:: Table Title
        :file: demo.csv
        :widths: 30, 30, 40, 1
        :header-rows: 1



**效果**

.. topic:: list
    :class: style-demo

    .. csv-table:: Table Title
        :file: demo.csv
        :widths: 30, 30, 40, 1
        :header-rows: 1

图片
=========

.. code-block:: rst

    .. image:: /images/project-image.png

**效果**

.. topic:: list
    :class: style-demo

    .. image:: /images/project-image.png

