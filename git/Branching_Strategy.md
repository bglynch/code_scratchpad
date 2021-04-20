# Branching Strategy

# Why

For a development team to accomplish work in a consistent and productive manner, a defined Git Workflow is required to agree how the flow of change will be applied.

This workflow needs to clearly define two discrete processes under a single agreed strategy:

1. When are where to **branch** from master
2. How and when to **merge via pull requests**
# Goal

To settle on an efficient Git Workflow that works for Philips eCommerce, while enabling/ensuring:

- collaboration and sharing of code
- isolation of work in progress from completed work
- changes are built, validated, and verified before they get to master
- preservation of important branches - master, releases, etc. - through access control and pull requests
- publishing, sharing, reviewing, and iteration of code in a simple and consistent manner
- less time managing version control, and more time developing code
# Considerations

Some things to consider when evaluating a Git workflow are:

- Does this workflow enhance the effectiveness of the team(s), or is it a burden that limits productivity?
- Does this workflow scale with team(s) size and structure, while maintaining collective ownership?
- Is it easy to undo mistakes and errors with this workflow?
- Does this workflow impose any new unnecessary cognitive overhead to the team?
# Principles
- Short-lived branches - minimise deviation from production/master branch, promoting cleaner merges and deploys. i.e. reduce risk of merge conflicts and deployment challenges.
- Merging & branching activities clearly defined as core part of developers’ *daily* workflow
- Isolate new features and bug fixes, either through branching or feature toggles
- Merge into important branches through Pull Requests only
- Minimize and simplify reverts
- Match a release schedule
- Maintain a high quality, up-to-date master branch; which is always in a deployable state
# As Is / Current Reality
## Branching Strategy

The following process is currently documented on Sharepoint:

![From ‘Development Process’ on Sharepoint](https://paper-attachments.dropbox.com/s_ADE88C8C755F8A32C5C1761C1FA7B9BAA2FF263612C1DE10C7B23F1DA844CDA1_1558522326754_image.png)


**Observations**

- with heavy focus on the release cycle, the `release` branch has become a main/primary branch, leaving `master` in an uncertain state
- without automated validation and verification of code, merges are difficult to verify, resulting in `release` branch regularly becoming inconsistent and of low quality
- `feature` branches from `master` without sufficient validation and verification of code and/or a consistent feature toggling approach, further contributes to issues with consistency and quality
- no defined process for managing bug-fixes in route to live or hot-fixes in Production
- understanding of current process across the teams is poor, leading to inconsistent approach to branching and merging at a team and developer level
## Pull Requests

The following process is currently documented on Sharepoint:

![From ‘Azure DevOps - Pull Request’ on Sharepoint](https://paper-attachments.dropbox.com/s_ADE88C8C755F8A32C5C1761C1FA7B9BAA2FF263612C1DE10C7B23F1DA844CDA1_1558967790873_image.png)

![From ‘Azure DevOps - Pull Request’ on Sharepoint](https://paper-attachments.dropbox.com/s_ADE88C8C755F8A32C5C1761C1FA7B9BAA2FF263612C1DE10C7B23F1DA844CDA1_1558968150311_image.png)


**Observations**

- defined process, but only loosely followed/understood by development teams
- increased guidance needed to connect process with Agile ways of working, specifically the definition of done
- increased guidance on purpose of pull requests, and the responsibility of the reviewers
- no defined impact for failure to meet purpose and responsibilities
# The Case for Change
## Individual Behaviours
## Team Behaviours
# Options
- Centralized
- Feature Branch
- Gitflow
- Forking
- GitHub flow
- Release Flow (recommended by Azure)
# To Be / Future Vision
## Direction

Following conversation between members of the eCommerce System Team (Lakshmi, Bart, Keith, Bartosz), agreement was made to move to Gitflow model.

Gitflow will introduce a very structured process, defining a hierarchy of branches and a protocol for merging code. The model will provide the stability required to follow a defined release process, while still providing a high-level of freedom for developers to be productive.

**Note:** This workflow will need to be iterated upon in the future if we are to move closer to Continuous Delivery, i.e. GitHub flow, Trunk-based Development. Before doing so, we will need to implement/explore:

- reliable and effective test automation suite
- continuous integration
- feature toggles - splicing work into self-contained changes, controlled with a flag/configuration
- branch by abstraction - leveraging the power of interfaces to isolate change
- splitting the work - designing as separate modules, components, services to isolate change
## Gitflow
- Git workflow first published by Vincent Driessen at nvie
- Strict branching model design around a scheduled release cycle
- Provides a robust framework for managing larger projects
- Extends Feature Branch Workflow, to include individual branches to prepare, maintain, and record releases
- Includes benefits of Feature Branch Workflow - pull requests, isolated experiments, efficient collaboration 
## Main branches

Main branches have an infinite lifetime, and exist in parallel

- `master`
    - main branch where the source code of `HEAD` always reflects a *production-ready* state.
    - stores official release history
- `develop`
    - main branch where the source code of `HEAD` always reflects a state with the latest delivered development changes for the next release
    - serves as integration branch for new features
    - where automated build and deploy should run from  
![main branches](https://paper-attachments.dropbox.com/s_ADE88C8C755F8A32C5C1761C1FA7B9BAA2FF263612C1DE10C7B23F1DA844CDA1_1558969249444_image.png)

## Supporting branches

Supporting branches have a limited lifetime, and exist to:

- aid parallel development between team members
- ease tracking of features
- prepare for production releases
- assist in quickly fixing production issues

There are different types of supporting branches that may be used:

- `feature` branches
- `release` branches
- `hotfix` branches

Each of which has a specific purpose and are bound to strict rules as to which branches may be their originating branch and which branches must be their merge targets.


## Feature branches
- Used to create features for an upcoming or distant future release
- Only exist as long as the feature is in development
- Will eventually be either merged back into `develop` on completion or discarded as a disappointing experiment

**Rules:**

- Must branch off from: `develop`
- Must merge back to: `develop`
- Branch naming convention: `feature/[workitem-id]-[workitem-title]`  
![feature branches](https://paper-attachments.dropbox.com/s_ADE88C8C755F8A32C5C1761C1FA7B9BAA2FF263612C1DE10C7B23F1DA844CDA1_1558969285772_image.png)

## Release branches
- Used to support preparation of a new planned production release
- Only exists as long as the release needs to be supported in production
- Allows for the preparation of a release cycle, while allowing work for the next release to continue on `develop`
- Once `release` is created from `develop`, only minor bug fixes may be applied
    - new features must merge back to `develop` and await the next release
- When `release` is ready for release, it is merged back to both `master` and `develop`, with a tag created in `master`

**Rules:**

- Must branch off from: `develop`
- Must merge back to: `develop` and `master`
- Branch naming convention: `release/[release-version]`  
![](https://paper-attachments.dropbox.com/s_ADE88C8C755F8A32C5C1761C1FA7B9BAA2FF263612C1DE10C7B23F1DA844CDA1_1558969352840_image.png)

## Hotfix branches
- Used to support the release of a new unplanned production release
- Only used as a necessity to act immediately on an undesired state in live production
- Allows work to continue on `develop` for next release while production issue is being resolved

**Rules:**

- Must branch off from: `master`
- Must merge back to: `master` and `develop` or `release` (depending on whether a release branch exists)
- Branch naming convention: `hotfix/[workitem-id]-[workitem-title]`  
![](https://paper-attachments.dropbox.com/s_ADE88C8C755F8A32C5C1761C1FA7B9BAA2FF263612C1DE10C7B23F1DA844CDA1_1558969385759_image.png)

## Pull Requests
- designed to encourage and capture conversation:
    - what is being changed and why, as continuous knowledge sharing
    - drive alignment of best practice, code styles, quality standards, etc.
- can be opened at any point in the development process:
    - when you have little or no code but want to share some screenshots or general ideas
    - when you're stuck and need help or advice
    - or when you're ready for someone to review your work
- encourage high quality feedback, to create high quality reviews
    - ensure the right people review the pull request
    - ensure that reviewers know what the code does
    - give actionable, constructive feedback
    - reply to comments in a timely manner
- to enable continuous collaboration and code review, it is good practice to open pull requests as early as possible, discussing implementation details and architecture choices on the go
# How do we get there?
- agree on this strategy, and resolve open items:
    - how `develop` branches are needed?
    - what naming convention fits best for branches?
- identify opportunity to begin implementation - most likely after next release
- roll-out plan for policy enforcement
- communicate to teams regarding upcoming change
- educate teams on new strategy
- provide walkthrough guide to branch and merge, including pull request
## Branch Naming Convention
- Define and socialise naming convention
- Enforce convention through policies
    - including folder structure
- roll-out plan, leverage folder structure
    - rename or iterate
## Branch Policies
- Pull Requests
    - Pull Request template to guide reviewer
    - Pull Request reviewer policies
        - minimum number of reviewers
        - restrict self-approval
        - restrict completion if a reviewer votes to wait or reject
        - reset voting if changes pushed
    - Pull request linked to Work Item
    - Pull request comments have been resolved
    - Merge strategy
        - no-fast-forward vs squash
    - Build validation of Pull Requests
    - Automatically include reviewers

# References
| Title                                        | Link                                                                                                          |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| gitworkflows                                 | https://git-scm.com/docs/gitworkflows                                                                         |
| Comparing Workflows                          | https://www.atlassian.com/git/tutorials/comparing-workflows                                                   |
| Gitflow Workflow                             | https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow                                  |
| A successful Git branching model             | https://nvie.com/posts/a-successful-git-branching-model/                                                      |
| Understanding the GitHub flow                | https://guides.github.com/introduction/flow/                                                                  |
| Adopting a Git branching strategy            | https://docs.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops              |
| Review code with Pull Requests               | https://docs.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops                       |
| Require branches to be created in folders    | https://docs.microsoft.com/en-us/azure/devops/repos/git/require-branch-folders?view=azure-devops&tabs=browser |
| Improve code quality with branch policies    | https://docs.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops                     |
| Improving on Gitflow for Continuous Delivery | https://www.infoworld.com/article/2909346/improving-on-git-flow-for-continuous-delivery.html                  |
| A Git Workflow for Continuous Delivery       | https://blogs.technet.microsoft.com/devops/2016/06/21/a-git-workflow-for-continuous-delivery/                 |
| Feature Toggles                              | https://martinfowler.com/articles/feature-toggles.html                                                        |
| Branch by Abstraction                        | https://martinfowler.com/bliki/BranchByAbstraction.html                                                       |


