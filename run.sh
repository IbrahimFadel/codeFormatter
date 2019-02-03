#!/bin/bash
echo Thank you for using this code formatter!
{ # try
	echo Compiling
	python3 compiler.py
	echo Success
} || { # catch
   echo Could not compile
}