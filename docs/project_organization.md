# Project management

- [Project management](#project-management)
    - [Zenhub](#zenhub)
        - [Browser Extension](#browser-extension)
        - [Standalone Webapp](#standalone-webapp)
    - [Scrum & Git Workflow](#scrum--git-workflow)
        - [Scrum Meetings](#scrum-meetings)
        - [Commits & Branching](#commits--branching)

## Zenhub
For our project management and our own Scrum workflow we are using [Zenhub](https://zenhub.com). ZenHub is a independent project management tool natively integrated with GitHub. Their seamless platform is powered by our own GitHub data, so everything gets updated automatically.

You can use Zenhub on two different ways:
1. Use the browser extension for Chrome or Safari (maybe also for Firefox?) (https://www.zenhub.com/extension)
2. Use the standalone webapp (https://app.zenhub.com/)

### Browser Extension
The browser extension adds the Zenhub webapp into the GitHub website and extends the GitHub issues with some additional fields like Pipeline, Estimate, Release Epics.

### Standalone Webapp
The standalone webapp has no specific functionality which isn't available in the extended GitHub UI.


## Scrum & Git Workflow
In the Scrum context we are working with the following synonyms:
- Epic = User Story
- Issues = Tasks

### Scrum Meetings
| Scrum Meeting  |                                                                         Description                                                                         |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Planning       | At the beginning of a sprint                                                                                                                                |
| Weekly         | A weekly meeting which is like a daily (short and compact)                                                                                                  |
| Review & Retro | At the end of a sprint                                                                                                                                      |
| Refinement     | Sometimes. This is the point, where we try to fill the missing position of a PO. We are discussing the next User Stories and creating Tasks for this story. |

### Commits & Branching
For every Epic the developer has to create an separate branch. The name of this branches are always to define appending to this format: `feat-{id}` (`{id}` has to be replaced with the issue Epic number (Issue Number)).

The commit messages have to be in this format: `#{id}: Message` (`{id}` has to be replaced with the issue number). Please try to tell what was added/changed/edited/removed and why this has to be.