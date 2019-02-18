.. image:: image_github.png

Getting Started
---------------

Create an account at `Github <https://github.com>`_. Create a new project (e.g. first). Copy the link to the project which should look like `https://github.com/username/projectname.git`.
On the local machine create a directory with the same name as that of the repository name. 
Add files to the project directory.
Install git.

.. code::

	sudo apt-get install git

Name your github account as
 
.. code::

	git config --global user.name "Name"

Add the email address to your github account by

.. code::

	git config --global user.email "Email"

Now move to the project directory in the command line.

Follow the following commands to modify the entries to the remote project directory.

.. code::

	git init
	git add *
	git commit -m "Comment about the change"
	git remote add origin https://github.com/username/projectname.git
	git push -u origin master

To remove any file at the remote repository

.. code::

	git rm file1.txt
	git commit -m "removal comments"

This page is built using `Sphinx <https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html>`_.

