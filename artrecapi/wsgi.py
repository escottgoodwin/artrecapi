from application import application
from random import randint
import os
from bs4 import BeautifulSoup
import json
from textblob import TextBlob
from gensim.models.doc2vec import Doc2Vec,TaggedDocument
import datetime
import requests
import json
from stop_words import get_stop_words
import pymongo
import boto3
from scipy.spatial.distance import cosine
import goslate
import botocore
import psycopg2
import numpy as np
from operator import itemgetter
import pandas as pd
from flask import Flask, render_template, Response, request, redirect, url_for,session

if __name__ == "__main__":
    application.run()
