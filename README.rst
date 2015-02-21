pck - A package development framework
=====================================

``pck`` - A package development framework for Python.

Motivation
==========

Packaging contains tons of boilerplates.
Preparing continual development enviroment requires wide-ranging knokledges.

* ``pck`` is not just a scafolding tool, but a package development framework.

not for aliens, mummies and insane clowns, but for humans.

Usage
=====

* pck [i]nit  # Scaffold the project step by step.

  * setup.py
  * tox.ini
  * venv
  * \.(git|hg)ignore
  * README
  * CHANGES
  * LICENSE
  * MANIFEST.in
  * setup.cfg
  * .coveragerc

* pck  # Activate the venv
* pck [q]uit # Deactivate the venv
* pck [r]un  # Run python command with the venv
* pck [v]ersion  # Checking updates of requirements.
* pck [r]eadme  # Build README doc.
* pck [d]ocs  # Build the docs.
* pck [t]est  # Run the tests.
* pck [p]ublish  # Create sdist package and upload it.
* pck [w]atch test  # Run the watch doc for the project and run commands

And some utilities.

* pck venv  # Show the path to venv
* pck why  # Show the motivation of pck
* pck atsuo  # Show atsuoishimoto
