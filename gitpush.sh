#!/bin/bash

echo reset
git reset

git config --global user.email "dev@realmethods.com"
git config --global user.name "Scrum Master"
 
echo init the repository
git init

echo add all files from root dir below, with ignore dirs and files in the .gitignore
git add .

echo 'commit all the files'
git commit -m "initial commit"

echo 'add a remote pseudo for the Django repository'
git remote add Django https://complexmathguy:6969Cutlass!!@github.com/complexmathguy/Django

echo 'push the commits to the repository master'
git push Django master

echo 'delete tag latest'
git tag -d latest
git push --delete Django latest

echo 'add tag latest'
git tag latest

echo 'push tag latest'
git push Django latest

