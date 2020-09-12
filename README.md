# MultiTool

# RULES #

Welcome! If you are reading this, then you or someone believes you are capable of adding to this project. Honestly, that is the hardest step...
1. if you want to make any changes, CREATE ANOTHER COPY AND EDIT THAT! This is especially true if you do not have access to another copy.
2. this file will be divided up by script and comment numbers like this --> **ScriptName:#**. This method is used to explain in more detail what that comment is trying to say.
3. any changes you make, please comment and update this subsequently. The intention behind designing this script, how I have, is to make it as modifiable and updatable as possible. If you don't I will find you and I will make you comment!
4. This README is only for Multitool not for any of the tools. Each tool has it's own README and those should be updated.
5. Each change you make must be noted in the **CHANGELOG** section with the version number. Version number convention is ->
   **Major_Changes.Minor_changes.patches/bug_fixes.smallest**. Please update!
6. Shameless plug, if you don't know python link to my Youtube series teaching it [HERE][f1ccf610]

  [f1ccf610]: https://www.youtube.com/channel/UCZfKpmqhZy1mlaFQu4jiCbA?view_as=subscriber "My Youtube channel"

# GOAL OF PROJECT #

The goal of this script is to make scripts used for HelpDesks easily accessible and able to be ran in rapid succession. Each script within the options folder should be accessible by python; this allows ease of execution. This attempts to combine scripts that can be run individually and allow them to run in tangent as well. The goal is to make this project as easily expandable as possible, encouraging contributions.

# COMMENTS EXPLAINED #
## optionMenu.py ##
- optionMenu:01 - Selected is a list of scripts that the user wants to run. The list defaults as empty, because the user does not have to run any scripts. Every selection made will be added to this list, until "start" is selected.
- optionMenu:02 - Options list parses the "Options" folder for potential options. **ALL** scripts that are options must be in here as an exe.
- optionMenu:03 -
- optionMenu:04 - It checks if any options are in the selected list, if they are it is indicated by [x] instead of [ ] before the name.
- optionMenu:05 - formats how the GUI will display for the user.
- optionMenu:06 -
- optionMenu:07 -
- optionMenu:08 -
- optionMenu:09 -
- optionMenu:10 -
- optionMenu:11 -
- optionMenu:12 -
- optionMenu:13 -
- optionMenu:14 -
- optionMenu:15 -
- optionMenu:16 -
- optionMenu:17 -
- optionMenu:18 -
- optionMenu:19 -
- optionMenu:20 -
- optionMenu:21 -

# CHANGELOG #
## DRAFT VERSIONS ##
### Version 1 ###
- Draft 1.0.0.0 - Starting version of the script
- Draft 1.0.0.1 - Added RunOrderList.txt to indicate what order the script should run the options
- Draft 1.0.0.2 - Changed RunOrderList.txt to scriptInfo.xml. Any scripts added this multitool should have an accompanied sciptInfo.xml formatted the same way.
- Draft 1.0.0.3 - Added comments to Multitool
- Draft 1.0.1.0 - Added OpeningScreen class using xml to fill in info
- Draft 1.0.1.1 - Reinstated RunOrderList.txt, this txt will be used to order the script types for run order.
- Draft 1.0.2.0 - Changed scriptInfo.xml to projectInfo.xml, change was made to reduce amount of xml documents requiring parsing.
- Draft 1.0.3.0 - Added scripts class to grab information from xml file about each script included.
- Draft 1.0.3.1 - Added terminal updates after each selection.
- Draft 1.0.3.2 - adjusted xml, optionMenu.py will be selected by type. All scripts will be encased in <script>
#### Version 1.1 ####
