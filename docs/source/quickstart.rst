====================
Quick Start
====================

在这篇文档中主要说明了如何安装我们的主题，以及如何利用 *sphinx-quickstart* 来生成一个文档项目，并进行基础的配置。

安装
================

`THUNLP Docs` 模板有两种安装方法

使用PIP安装（推荐）
-----------------------

.. code-block:: sh

    pip install sphinx_thunlp_theme

使用setup.py安装
-----------------------

首先将本项目clone到本地，然后进入到项目目录中，输入以下命令：

.. code-block:: sh

    python setup.py install


生成文档模板
====================

安装好 *sphinx_thunlp_theme* 之后，进入自己要编写文档的项目目录。

通常文档会被存放在一个单独的目录中，因此我们推荐你建立一个 **docs** 文件夹，并使用 *sphinx-quickstart* 在目录下生成一个模板（建议选择使用独立的源文件和构建目录）。

.. code-block:: sh

    mkdir docs
    sphinx-quickstart

跟随 *sphinx-quickstart* 的指引，可以建立起一个简单的文档模板。

使用 sphinx_thunlp_theme 
==================================

在 *source* 目录下找到配置文件 *conf.py* ，修改如下内容：

.. code-block:: python

    html_theme = "sphinx_thunlp_theme"

即可引入 `THUNLP Docs` 主题。

使用 THUNLP Docs 首页模板
======================================

开源项目首页对应了源代码文件 *index.rst* ，*index.rst* 文件使用 **reST** 语言编写，在本篇教程中不会详细的介绍它的用法，不过你可以在 `reST` 章节中学习。

在使用 `THUNLP Docs` 模板时，我们对首页的内容有一些具体的要求，它通常需要包含以下部分的内容。

项目名称
-------------------

项目名称也就是 *index.rst* 文档的标题，在文档中通常使用`=`来作为分隔符，在项目名称的上一行和下一行加入长度相等且超过项目名称长度的 *"="* 即可。

.. code-block:: rst

    =====================
    Your Project Name
    =====================

Topic Tree
---------------------

Topic Tree是整个文档的目录，它可以是一个多层级的结构，用于构建层次化的导航。在 `THUNLP Docs` 中对应了上方导航栏部分，是一个必要的项目。

在使用 `THUNLP Docs` 模板的时候，你需要编写以下代码

.. code-block:: rst

    topic-trees
    ========================

    .. toctree::

        Home <self>
        Quick Start <quickstart>


    .. toctree::
        :caption: Examples

        Example 1: Basic Usage <examples/example1>
        Example 2: Customized Victim Model <examples/example2>
        Example 3: Customized Attack Model <examples/example3>

    .. toctree::
        :caption: Modules

        DataManager <apis/data_manager>
        Attacker <apis/attacker>
        Substitute <apis/substitute>

在模板中，我们支持同时存在多个 `toctree` ，每个 `toctree` 可以是匿名的也可以是具有 `caption` 属性的。

在匿名的`toctree`中，每一个跳转向其它页面的链接会被直接的显示在页面上方的导航栏中；而在具有 `caption` 属性的 `toctree` 中，它的所有链接会被折叠成一个下拉菜单，只在顶部导航栏中显示 `caption` 属性的内容。

在编写过程中，请不要改动 ``topic-trees`` 这个名字，它对于首页模板的生成很重要。


项目的口号
--------------------

在使用 `THUNLP Docs` 模板时，你需要设计好两句项目的口号，一句短一些的和一句长一些的。除此之外还需要准备一张项目的配图，配图的大小需要正好是 ``500 x 500`` 像素。

这些内容会显示在项目首页的开头，是让其它人了解你的项目的最快捷的途径。它在首页中对应了以下的代码

.. code-block:: rst

    project-slogans
    ========================

    .. topic:: project slogan short
        :class: project-slogan-short

        An Open-Source Package for Neural Relation Extraction

    .. topic:: project slogan long
        :class: project-slogan-long

        OpenNRE is an open-source and extensible toolkit that provides a unified framework to implement relation extraction models. 

    .. image:: images/project-image.png
        :class: project-image

    .. topic:: install link
        :class: link-button

        :doc:`Install</quickstart/installation>`

    .. topic:: quickstart link
        :class: link-button

        :doc:`Quick Start</quickstart/introduction>`

在实际项目文档编写过程中，可以根据需求替换其中的某些部分，例如添加一些链接按钮（论文链接、项目源代码仓库）等等。


项目的特点
--------------------

项目特点部分会显示在项目口号部分的下方，呈现为横向的排版模式。 通常，准备三个项目特点会在排版上显得最为美观，过多的特点数量和过少的特点数量都会在展示和呈现的时候给人一种奇怪的感觉。

这部分主要对应了以下的代码

.. code-block:: rst

    project-features
    ========================

    .. topic:: project-feature-1
        :class: project-feature

        .. image:: images/project-feature-1.svg

        高效

            基于rst语法方便的富文本编写，模板化的项目首页，帮助开发者快速的构建项目专属网站。

    .. topic:: project-feature-2
        :class: project-feature

        .. image:: images/project-feature-2.png

        易迁移

            基于Sphinx theme开发，可以实现和原生theme的无缝切换，也可以在本地、云端、github pages和readthedocs无缝部署！
    

    .. topic:: project-feature-3
        :class: project-feature

        .. image:: images/project-feature-3.svg

        可扩展

            多种Sphinx插件任你选！autodoc、coverage、todo、viewcode ... 让文档编写更简单！

你需要为每个项目特点准备一个小图标，图标的高度在 ``40`` 像素左右为最佳，配色推荐使用 ``#1185A7`` （对应RGB ``17,133,167`` ）。
除此之外，每一个特点都需要准备一段话来进行简单介绍，它会被展示在特点名称下方。

功能介绍
-------------------

功能介绍板块是一个可选的内容，它主要包含了若干个功能介绍内容。每个功能介绍内容包含了一张图片和一段文字描述，其中图片的宽度最好为 ``300`` 像素。

在实际展示中，你可以根据自己的需求将图片放在左侧或者右侧，具体的代码内容参考如下：

.. code-block:: rst

    project-introduction
    ========================
    .. topic:: project-intro-1
        :class: image-left

        .. image:: images/project-intro-1.png

        项目内容页面采用了两级目录浮动侧边栏，可以实现智能的跟随移动，点击跳转功能。

    .. topic:: project-intro-2
        :class: image-right

        .. image:: images/project-intro-2.png

        专业配色样式的代码文档高亮，支持viewcode扩展实现API和代码的链接跳转，提供代码阅读全新体验！

每一个topic对应了一项功能介绍，你可以通过修改 ``image-left`` 和 ``image-right`` 来控制图片实际显示的位置。


数据展示
----------------------

在介绍项目时，我们通常也会有项目指标的介绍。在这里，我们提供了一个数据展示板块，你可以通过自己的编写相关介绍准备图片来进行一个展示。

所有数据项会按横向排版，通常展示3～4个数据项会在排版上显得更好看。除此之外，你还可以准备一段话来介绍说明以下你的数据指标的评测环境等等，它会被居中展示在数据指标的上方。

参考如下代码：

.. code-block:: rst

    data-results
    ========================

    Data Results
    --------------

    .. topic:: data results
        :class: align-center

        Nunc porta erat ut lectus posuere molestie. Vestibulum risus ligula, rhoncus eleifend rhoncus sed, malesuada id metus. Aenean lorem nibh, varius fermentum viverra vel, efficitur nec elit. Nunc porta erat ut lectus posuere molestie. Vestibulum risus ligula, rhoncus eleifend rhoncus sed, malesuada id metus. Aenean lorem nibh, varius fermentum v

    .. topic:: data result list
        :class: data-result

        .. container::

            .. image:: images/project-results-1.png

            Nunc porta erat ut lectus posuere molestie. Nunc porta erat ut 
    
        .. container::

            .. image:: images/project-results-2.png

            Nunc porta erat ut lectus posuere molestie. Nunc porta erat ut 
    
        .. container::

            .. image:: images/project-results-3.png

            Nunc porta erat ut lectus posuere molestie. Nunc porta erat ut 
    
        .. container::

            .. image:: images/project-results-4.png

            Nunc porta erat ut lectus posuere molestie. Nunc porta erat ut 

最终渲染的样式如下：

.. image:: /images/introduction-data-result.png


相关文章
-------------------

在首页的末尾，你还可以添加相关文章的列表，用于链接到一些其它网站上的博客等等。 对于每一篇相关文章，你需要准备一张文章的介绍图，文章的标题和链接，以及文章的内容简介。 文章的介绍图最佳尺寸是 ``370 x 300`` 像素，文章的数量最好为3篇。

具体添加方法请参考以下代码：

.. code-block:: rst

    related-articles
    ========================

    Related articles
    -----------------

    .. topic:: related articles
        :class: related-articles

        .. container::

            .. image:: images/project-related-1.png

            `OpenAttack <https://github.com/thunlp/OpenAttack>`_

                David Bowie once speculated about life on Mars, and now NASA scientists are wondering the same thing about
    
        .. container::

            .. image:: images/project-related-2.png

            `OpenAttack <https://github.com/thunlp/OpenAttack>`_

                David Bowie once speculated about life on Mars, and now NASA scientists are wondering the same thing about
    
        .. container::

            .. image:: images/project-related-3.png

            `OpenAttack <https://github.com/thunlp/OpenAttack>`_

                David Bowie once speculated about life on Mars, and now NASA scientists are wondering the same thing about
    

完整的样例代码
=========================

.. code-block:: rst
    :linenos:
    :name: index.rst

    =====================
    Your Project Name
    =====================

    topic-trees
    ========================

    .. toctree::

        Home <self>
        Quick Start <quickstart>


    .. toctree::
        :caption: Examples

        Example 1: Basic Usage <examples/example1>
        Example 2: Customized Victim Model <examples/example2>
        Example 3: Customized Attack Model <examples/example3>

    .. toctree::
        :caption: Modules

        DataManager <apis/data_manager>
        Attacker <apis/attacker>
        Substitute <apis/substitute>

    project-slogans
    ========================

    .. topic:: project slogan short
        :class: project-slogan-short

        An Open-Source Package for Neural Relation Extraction

    .. topic:: project slogan long
        :class: project-slogan-long

        OpenNRE is an open-source and extensible toolkit that provides a unified framework to implement relation extraction models. 

    .. image:: images/project-image.png
        :class: project-image

    .. topic:: install link
        :class: link-button

        :doc:`Install</quickstart/installation>`

    .. topic:: quickstart link
        :class: link-button

        :doc:`Quick Start</quickstart/introduction>`

    project-features
    ========================

    .. topic:: project-feature-1
        :class: project-feature

        .. image:: images/project-feature-1.svg

        高效

            基于rst语法方便的富文本编写，模板化的项目首页，帮助开发者快速的构建项目专属网站。

    .. topic:: project-feature-2
        :class: project-feature

        .. image:: images/project-feature-2.png

        易迁移

            基于Sphinx theme开发，可以实现和原生theme的无缝切换，也可以在本地、云端、github pages和readthedocs无缝部署！
    

    .. topic:: project-feature-3
        :class: project-feature

        .. image:: images/project-feature-3.svg

        可扩展

            多种Sphinx插件任你选！autodoc、coverage、todo、viewcode ... 让文档编写更简单！


    data-results
    ========================

    Data Results
    --------------

    .. topic:: data results
        :class: align-center

        Nunc porta erat ut lectus posuere molestie. Vestibulum risus ligula, rhoncus eleifend rhoncus sed, malesuada id metus. Aenean lorem nibh, varius fermentum viverra vel, efficitur nec elit. Nunc porta erat ut lectus posuere molestie. Vestibulum risus ligula, rhoncus eleifend rhoncus sed, malesuada id metus. Aenean lorem nibh, varius fermentum v

    .. topic:: data result list
        :class: data-result

        .. container::

            .. image:: images/project-results-1.png

            Nunc porta erat ut lectus posuere molestie. Nunc porta erat ut 
    
        .. container::

            .. image:: images/project-results-2.png

            Nunc porta erat ut lectus posuere molestie. Nunc porta erat ut 
    
        .. container::

            .. image:: images/project-results-3.png

            Nunc porta erat ut lectus posuere molestie. Nunc porta erat ut 
    
        .. container::

            .. image:: images/project-results-4.png

            Nunc porta erat ut lectus posuere molestie. Nunc porta erat ut 

    related-articles
    ========================

    Related articles
    -----------------

    .. topic:: related articles
        :class: related-articles

        .. container::

            .. image:: images/project-related-1.png

            `OpenAttack <https://github.com/thunlp/OpenAttack>`_

                David Bowie once speculated about life on Mars, and now NASA scientists are wondering the same thing about
    
        .. container::

            .. image:: images/project-related-2.png

            `OpenAttack <https://github.com/thunlp/OpenAttack>`_

                David Bowie once speculated about life on Mars, and now NASA scientists are wondering the same thing about
    
        .. container::

            .. image:: images/project-related-3.png

            `OpenAttack <https://github.com/thunlp/OpenAttack>`_

                David Bowie once speculated about life on Mars, and now NASA scientists are wondering the same thing about
    