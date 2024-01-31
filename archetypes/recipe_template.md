---
draft: true # Use this only for setting draft status
hidden: false # Use this to hide unwanted recipes
slug: # <post-title>
title: '{{ recipe.title }}'
description: "{{ recipe.description }}"
image: {{ recipe.image }}
date: {{ recipe.date }}
author: {{ recipe.author }}

tags: {{ recipe.tags }}
categories: "{{ recipe.categories }}"
cuisines: "{{ recipe.cuisines }}"
allergens: {{ recipe.allergens }}

calories: {{ recipe.calories }}
preptime: {{ recipe.preptime }}
cooktime: # 180 = 3 Hours | In minutes
totaltime: {{ recipe.totaltime }}
servings: {{ recipe.servings }}

links:
  - description: "{{ recipe.linkDescription }}"
    website: {{ recipe.linkUrl }}
    image: {{recipe.image }}
 
weight: # 1 | You can add weight to some posts to override the default sorting (date descending)

comments: false # Keep False

ingredients: {{ recipe.ingredients }}

instructionTitles: {{ recipe.instructionTitles }}
instructions: {{ recipe.instructions }}
---