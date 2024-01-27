---
type: recipe # Points to \layouts\recipe\
layout: single # Sets layout to {type}\single.html

draft: false # Use this only for setting draft status
hidden: false # Use this to hide unwanted recipes
slug: template
title: Template
description: Sample recipe layout.
image: cover.png # Local image or URL
date: 2022-03-06 00:00:00+0000
author: # Recipe Author or Organization (John Doe, HelloFresh)

tags: [] # Description, Season, Holiday (quick, easy, summer, christmas)
categories: [] # Main, Dessert, Snack, Dinner
cuisines: [] # Region (French, American, Mediterranean)

calories: 500
preptime: 10
cooktime: 60
servings: 6

links:
  - title: # AllRecipes
    description: # AllRecipes is the world's largest collection of shareable recipes.
    website: # https://allrecipes.com
    image: '{{< ogimage url="" >}}' # Dynamically updates the link image based on the website above.
    
weight: 1       # You can add weight to some posts to override the default sorting (date descending)

comments: false # Keep False
---