========================
Inline
========================

本篇主要介绍行内的一些常见文本标记，包括加粗、斜体、内联代码和公式等。

斜体
==============

.. code-block:: rst

    这是一个 *斜体* 。

**效果**

.. topic:: list
    :class: style-demo

    这是一个 *斜体* 。


**注意** ：在使用这些标记时，需要注意不要添加额外的空格，也不要遗漏必要的空格。

加粗
=================

.. code-block:: rst

    这是一个 **加粗** 。

**效果**

.. topic:: list
    :class: style-demo

    这是一个 **加粗** 。

内联代码
=================

.. code-block:: rst

    这是一个 ``内联代码`` 。

**效果**

.. topic:: list
    :class: style-demo

    这是一个 ``内联代码`` 。
    
外部链接
================

.. code-block:: rst

    这是一个外部链接 `THUNLP <https://nlp.csai.tsinghua.edu.cn/>`_ 。

**效果**

.. topic:: list
    :class: style-demo

    这是一个外部链接 `THUNLP <https://nlp.csai.tsinghua.edu.cn/>`_ 。

内部链接
=====================

内部链接需要先在文档的对应位置打上标记，它的格式如下：

.. _my-reference-label:

.. code-block:: rst

    .. _my-reference-label:

然后可以在其它地方引用它：

.. code-block:: rst

    这是一个内部链接 :ref:`Link <my-reference-label>` 。

**效果**

.. topic:: list
    :class: style-demo

    这是一个内部链接 :ref:`Link <my-reference-label>` 。

内部文档链接
===================

.. code-block:: rst

    :doc:`Title & Paragraph<title>`

**效果**

.. topic:: list
    :class: style-demo

    :doc:`Title & Paragraph<title>`


下载链接
==================

.. code-block:: rst

    点击这里下载 :download:`下载链接 <../index.rst>` 。

**效果**

.. topic:: list
    :class: style-demo

    点击这里下载 :download:`下载链接 <../index.rst>` 。


脚注
==================

**reST** 中，添加脚注需要在文本中插入 ``[#xxx]_`` 的样式，其中xx是脚注的名称。

.. code-block:: rst

    这是第一个脚注 [#note1]_ 除了它以外还有 ... [#note2]_

然后在文档的最后添加以下代码，用于编写脚注的详细信息：

.. code-block:: rst

    .. rubric:: 脚注

    .. [#note1] 这是第一个脚注
    .. [#note2] 这是第二个脚注

**效果**

.. topic:: list
    :class: style-demo

    这是第一个脚注 [#note1]_ 除了它以外还有 ... [#note2]_

    .. rubric:: 脚注

    .. [#note1] 这是第一个脚注
    .. [#note2] 这是第二个脚注

公式
===================

在 **reST** 中可以插入公式块或者内联公式。

公式块
-------------------

.. code-block:: rst

    .. math::

        \frac{ \sum_{t=0}^{N}f(t,k) }{N}


**效果**

.. topic:: list
    :class: style-demo

    .. math::

        \frac{ \sum_{t=0}^{N}f(t,k) }{N}

内联公式
-------------------

.. code-block:: rst

    上文 :math:`\frac{ \sum_{t=0}^{N}f(t,k) }{N}` 下文

**效果**

.. topic:: list
    :class: style-demo

    上文 :math:`\frac{ \sum_{t=0}^{N}f(t,k) }{N}` 下文