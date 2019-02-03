#!/bin/bash
{ # try
	pip install pyyaml
	echo installed pyyaml
} || { # catch
   echo could not install pyyaml
}