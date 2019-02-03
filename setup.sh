#!/bin/bash
{ # try
	echo installing pyyaml
	pip install pyyaml
	echo installed pyyaml
} || { # catch
   echo could not install pyyaml
}
