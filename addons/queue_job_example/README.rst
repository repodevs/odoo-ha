=================
Job Queue Example
=================

This addon add example for using Queue Job module


Installation
============

Go to ``Apps`` > search ``Queue Job Example`` then Install

Usage
=====

Make sure you already install odoorpc::

    pip install git+https://github.com/OCA/odoorpc@master


after installing odoorpc, use it::

    >>> import odoorpc
    >>> o = odoorpc.ODOO()
    >>> o.login('odoo', 'admin', 'admin')
    >>> o.execute('job.example', 'action_do', [])
    True
    >>> 

See job logs in menu ``Job Queue``
