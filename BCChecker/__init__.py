import os
from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from passlib.hash import sha256_crypt
import gc
from functools import wraps
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.models import model_from_json



app = Flask(__name__)


import BCChecker.views