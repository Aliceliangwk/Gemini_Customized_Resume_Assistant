________
title: Gemini Resume AI
emoji: 📉
colorFrom: indigo
colorTo: pink
sdk: streamlit
sdk_version: 1.34.0
app_file: app.py
pinned: false
license: apache-2.0
________


# Gemini_Customized_Resume_Assistant


After post covid, many jobs get affected and there's many layoffs. The job market is very competitive. as an employee and have been to this tough situation before, so i want to build a resume assistant app to help job seekers to stand out in the competitive and find their dream jobs.  

## What it does

a user just need  to fill out a job description, role, company name and upload a resume, then hit submit button. The app will utilize gemini api to analyze the job description to find out the top 3 responsibilities from the role and then provided a targeted resume for this application. 

## How we built it

i use the streamlit to build the interface and then use gemini api to analyze and generate a customized resume based on the uploaded resume. 

## Challenges we ran into

- it is my first time to use gemini api, it took me some time to learn how to call the api 
- when I tried to deploy the app on streamlit cloud, it run into permission problem and still couldn't figure it out yet. 

## Accomplishments that we're proud of: 

I built an app that actually can help millions of job seekers to stand out in the competitive job market and make a living in their lives. Also, i decided to build an app individually, so it would take me more time to learn and debug the app 

## What we learned

LEARN HOW TO USE gemini api and streamlit and how to deploy an app on cloud. 

## What's next for GeminiResume Boost
- resolve the permission issue on streamlit cloud and build a feature to see the matching scores of the uploaded resume and the job description. in addition, i want to add a feature to help job seekers to create targeted cover letters and help them save time and stand out in the competition .
