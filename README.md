# GA SEI Project 3: “Cake Sera, Sera” - Baked Goods Recipe-Sharing Community

### Deployed App: https://cakeprojectapp.herokuapp.com/

![cakesera](https://i.imgur.com/7ePFFoZ.gif)

#### Table of Contents
* Introduction
  * Brief and Requirements
  * Project Overview
  * Contributors
  * Timeframe
  * Technologies Employed
* Planning and Preparation
  * User Stories
  * Entity Relationship Diagram
  * Wireframe
* Development
  * Process
  * Featured Code
* Outcome
  * Challenges
  * Wins
  * Bugs
  * Future Inclusions and Improvements
  * Key Learnings


### Introduction

#### Project Requirements

* Work in a group of three to build a full-stack web application from scratch using the Django framework.
* Use Django, Python, HTML, CSS, JavaScript and an SQL database (PostgreSQL) to build the application in line with MVT architecture.
* Create the application using at least 2 related models, one of which should be a User.
* Include all major CRUD operations for at least one of your models.
* Add authentication AND authorization (page protection) to restrict access to relevant users, including the following features:
  * Users must be able to sign up or login.
  * Signed in users must be able to change their password and logout when finished with their session.
  * “Change password” and “logout” features must only be available to logged in users.
* Provide visual feedback to the user after each action, including after form submission success/failure.
* Layout and style your frontend with clean & well-formatted CSS, with or without a framework.

#### Project Overview
For this project, our team of three was required to create a full-stack application with the Django framework. We opted to create a website that would allow budding bakers to submit their variations of their favourite cakes and to browse recipes submitted by others. Unregistered visitors to the site would also be able to browse the full database, but without the option to add their own cakes or recipes.

The idea was to crowdsource recipes for both popular and more obscure cakes from a community of enthusiastic home bakers, also allowing for people to share variants that use novel ingredients or cater to different dietary requirements. If a registered user wishes to provide a recipe for a cake and the cake itself doesn’t already exist in the database, that user can create an entry for it themselves.


#### Contributors
* [Chris Ailey](https://github.com/C-T-Ailey)
  * [Archived obsolete project repository (See Day 4 of Development)](https://github.com/C-T-Ailey/Project-3-Cake-Recipe-Site/) 
* [Marc Usher](https://github.com/MarcUsher)
* [Richard Afrane-Kesey](https://github.com/richard70UKGithub)

#### Timeframe
This project was completed as a three-person group assignment over seven days.

#### Technologies Employed
* Python
* Django
* PostgreSQL with pgAdmin
* Bulma CSS Framework with additional custom CSS
* JavaScript and jQuery
* Git & GitHub
* Figma (Wireframes and flow graph)
* Trello (Project planning)
* Heroku (Deployment)

### Planning and Preparation

In order to ensure we had as clear a path through development as possible, we drafted a flow chart using Figma to map our routes through the various pages and CRUD operations we would require in our final build. Having this clearly laid out gave us a solid impression of the site flow, how our Entity Relationship Diagram would fit together, which areas of development to prioritise and how best to divide the workload between us.

![flowchart](https://i.imgur.com/DcoBuTn.jpg)
[Full flowchart available on Figma.](https://www.figma.com/file/m0UJ2ts4ymmX0cVTTCG6SS/Cake-Recipe-Site-Flowchart)

With planning the development process itself, we established a board on Trello where we could collate our resources and keep our User Stories available for ease of reference throughout. The team agreed that a twice-daily standup at the beginning and end of each day’s work would help us to stay informed on one another’s progress, and resolved to check in with each other at regular intervals, whether to push/pull updates or see if any other teammate required assistance. In the event one of us ran up against a difficult issue, we would go back to pair programming until the issue was resolved; this ensured that obstacles would be overcome as quickly as possible and everyone could proceed onto the next criteria, rather than leaving one teammate to struggle while the others pressed on with their own development. This flow would be repeated until completion - we would look at which pieces of the project remained incomplete, decide amongst ourselves which we felt most comfortable to attempt, and assisted each other in completing them whenever necessary.

#### User Stories
After settling on our concept for the application, we assembled a list of user stories to ensure we had a guide for the main points of functionality we wanted our users to experience.
* As an unregistered visitor, I want to be able to browse the cakes to see which ones I want to make.
* As an unregistered visitor, I want to be able to see the details of a cake to find out how to make it.
* As an unregistered visitor, I want to be able to sign up and log in as a registered user, so I can access the full user functionality of the site.
* As a registered user, I want to be able to add a new cake to the database so I can share it with others.
* As a registered user, I want to add my own recipes to existing cakes so others can see how I made it.
* As a registered user, I want to be able to edit/delete the cakes and recipes that I've added so they can stay up to date.


#### Entity Relationship Diagram
In order to understand which data we would need to store and access to achieve our desired functionality, we created an ERD to show the flow and interaction of our intended models for the app.

Our intended models were as follows:
* User: Registered users for the site, required for authorisation and authentication of user-generated CRUD operations. Referenced as a Foreign Key by both the Cake and Recipe models to designate the creator of those records.
* Cake: Data for individual cakes, required to be created before recipes can be attributed to them. Cake ID is referenced as a Foreign Key by each recipe attributed to them, and references the ID of the user who created the record as a Foreign Key. Shares a One to Many relationship with the Recipe model as one cake can be attributed to many recipes, but one recipe can only be attributed to one cake.
* Recipe: Data for individual recipes. References the ID of the user who created the record as a Foreign Key. Shares a Many to One relationship with the Cake model as many recipes can be attributed to one cake, but only one cake can be attributed to a recipe.

![cakeERD](https://i.imgur.com/mqSECl8.jpg)

#### Wireframing
For the first two days of development, we focused on establishing our key functionality and deprioritised styling, instead using the Materialize CSS Framework to implement basic placeholder styles. 
As we had all of our key functionality up and running by the third day, we then took the time to create wireframe models of how we wanted our final build to look. This would help ensure the whole team would be working towards the same design, and that we would have a consistent visual experience across our pages and elements. We also opted to use the Bulma CSS Framework for the final styling and design of the site, as research into Django-friendly CSS frameworks made it apparent to us that it was among the frontrunners, particularly for styling forms.

![cakewireframe](https://i.imgur.com/pFWwHxv.png)

[Full wireframe images available on Figma.](https://www.figma.com/file/TZoFGaVXjTqfhnrhjKanf3/Project-3---Have-your-cake-and-eat-it?node-id=0%3A1)

### Development

#### Process
#### Day 1 - Further Planning, Initialising the Codebase, CRUD Operations
As outlined above, the first day of development began with a group effort to finalise our plan. Once we had mutually settled on the project scope and each understood the work ahead, we started active programming with a tri-programming session in order to construct the bones of our application in line with MVT architecture – initial URL paths, our desired models, and a select few templates to serve as placeholders. Once we had reached a state where the app could be worked on individually, we consulted our flow chart, conferred on which features we were in a position to begin implementing, and each selected a part of the app to personally develop.

I elected to take on the CRUD operations for our Cake model, as this particular model was the linchpin of our application’s functionality. My experience with CRUD operations in my previous project made this a straightforward effort, and as Marc had completed the authentication and authorization features, I took the opportunity to pass his LoginRequired mixin as an argument for each operation so that only logged-in users would be able to make use of them. 

After establishing the CRUD operations, I started creating a navigation bar and added links for every accessible view we had created. The final order of business before wrapping for the day was to pair-program with Richard in attempting to implement the creation of new recipes, as he had been experiencing a persistent issue with the original “Add Recipe” functionality redirecting the user to a page where the cake ID relevant to the recipe was inaccessible. Unfortunately, this particular issue was too much for either of us to resolve in the remaining time for this session, and I ultimately ran aground on the same problems he had experienced. Feeling our nerves begin to fray, we decided we had made good progress for one day, and opted to pick back up the following morning.


#### Day 2 - Cake Index Pagination, Partial Recipe Deletion
During our morning standup, Marc resolved to take a turn at cracking the recipe creation problem, leaving me free to attempt implementing pagination into the cakes index page. We had agreed to include this feature once we came to the realisation that, practically speaking, it would be likely that such a site would eventually accrue more submissions than could be comfortably displayed on one page. Solving this problem came with the pleasant discovery that Django’s documentation covered everything we needed to know about using pagination, and that the documentation itself was extremely straightforward in following.

The remainder of my day was occupied by implementing deletion for recipes, along with what would prove to be a symptom of something worse further down the line. Though it was simple enough to get the majority of the deletion code implemented, there was a persistent issue with the cancellation option redirecting to the cakes index instead of the details page for the cake itself. After initially getting the feature working enough to remove the record from our database and committing my changes in Git, my teammates made me aware that somehow, Richard’s .env and .gitignore files were being included in his pushes to GitHub and consequently passed to us through his pull requests. After a considerable amount of time spent trying to prevent this, we finally had success in rearranging his file structure so the issue ceased; as previously mentioned, however, this was only a precursor to a much bigger issue when it came to the deployment process.

#### Day 3 - Complete Recipe Deletion, Recipe Pagination, Styling Preparations
With the .env/gitignore issue from the previous day resolved, I returned to attempting a fix for the recipe deletion operation. The issue was that both the “confirm” and “cancel” buttons in the confirmation page were deleting the record and redirecting the user to the cakes index page; through significant trial and error, I eventually discovered that – for some reason I still can’t discern – Django was handling both buttons as “confirm” regardless of their attributes. The solution was ultimately to simply wrap the “cancel” option in an anchor tag styled to resemble a button instead, which proved to work perfectly.

After this, I began work on adding pagination to the recipes container within the cake details pages. This proved to be largely the same as with the cake index page, with some minor adjustments required for the sake of paginating the data within another page. The completion of this, alongside my teammates completing the components they had elected to work on, meant that our site’s functionality was virtually complete. This meant we were free to start prioritising styling; so far, we had used the Materialize CSS framework for placeholder styling, but doing so had caused us to develop a distaste for how unfriendly it proved to be with custom CSS. After some research, Marc pointed us towards the Bulma framework, which by all accounts seemed to be a Django-friendly source of convenient styling without preventing us from adding our own where required. As such, I wasted no time stripping Materialize from the app and replacing it with the requirements for Bulma.

Feeling buoyed by completing all of our functionality requirements and having prepared ourselves for the styling portion of the process, we merged our respective code and readied ourselves for the final push.

#### Day 4 - Styling, Migrating Repositories, Deployment
With our functionality complete, we were able to spend our final day of development focusing on our styling and making adjustments to our code where we saw fit. I took responsibility for providing styles for the base.html and home.html templates, which involved selecting font families for the header, navigation and body, selecting a colour palette, and sourcing an image to present on our landing page. Though a lengthy process which took up most of the final day, it proved to be somewhat relaxing and therapeutic, perhaps owing to the sense of accomplishment in having little else to do besides styling.

This peace was, however, unfortunately broken when I stepped away from CSS briefly to deploy the project to Heroku; I encountered numerous issues in the process, which we eventually learned was due to each team member having a very slightly incorrect file structure, as Richard had experienced on Day 2; minor as the disorganisation was, it was just enough to prevent Heroku from being able to find the files it needed. Frustratingly, this issue could not be fixed with the little reorganisation the file structure needed, as the file structure present within our repositories made it unreasonably complicated to supplant the old with the new. Instead, our only recourse was to fix our file structure, create new repositories on GitHub for the corrected codebase, and conduct deployment from my new lead repository. This meant that the majority of our commit history ended up confined to an obsolete repository, which for archival’s sake has been linked above under my name in “Contributors”.

Once the deployment issues had been fixed and our application was correctly hosted, we spent the remainder of our day polishing the last elements which required further styling, merged and tested our final code and, when we were content with our results, updated the deployed app with it before taking our time in seeding our database with enough relevant data to adequately demonstrate the site’s functionality.

#### Featured Code

**The Cake and Recipe Models**

The Cake and Recipe models were among the first pieces of code I wrote for this project as part of our tri-programming session for initialising the codebase. As our entire app concept relied on these, it was agreed between us that it was logical to prioritise them.

Cakes have five properties: title, which provides the name for the cake in question; flavours, which is selected from the FLAVOURS tuple and supplies the primary flavour profile for the cake; description, which provides the description of the cake’s qualities; imageurl, which provides the source URL for the image to be displayed on its card in the cake index; and created_by, which is a Foriegn Key storing the ID of the user who created the cake record in question.
Recipes, meanwhile, have eight properties: title, which provides the title of the recipe; description, which provides the description of what sets the recipe apart from others; ingredients, which explains the ingredients required for the recipe; instructions, which details the process for replicating the recipe; imageurl, which supplies the source URL of the image for that recipe’s particular variation of the cake; created_by, which is a Foreign Key storing the ID of the user who created the recipe; created_date, which timestamps the recipe with the date and time of its creation; and cake, which is a Foreign Key storing the ID of the cake which the recipe in question has been attributed to.

Of note is that FLAVOURS is a tuple of tuples, each child tuple having a hex colour code at index 0 (used to provide the background colour for the description area on that cake’s card in the cake index) and the name of the flavour itself at index 1.

```py
FLAVOURS = (
    ('#f4f0d2', 'Plain Sponge'),
    ('#e8b26b', 'Caramel'),
    ('#d4a373', 'Chocolate'),
    ('#fff3c9', 'Cream Cheese'),
    ('#fad2e6', 'Fruit'),
    ('#d48c55', 'Spiced'),
    ('#fffeeb', 'Vanilla'),
    ('#f1b0ff', 'Experimental')
)
 
class Cake(models.Model):
    name = models.CharField(max_length=100)
    flavours = models.CharField(max_length=7, choices=FLAVOURS, default=FLAVOURS[0][0])
    description = models.TextField(max_length=250)
    imageurl = models.CharField(default=None, blank=True, max_length=300, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pk': self.id})
 
    def __str__(self):
        return f"{self.name}"
 
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True)
    ingredients = models.TextField(max_length=500)
    instructions = models.TextField(max_length=500)
    imageurl = models.CharField(default=None, blank=True, max_length=300, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
 
    def __str__(self):
        return f"{self.title} added to cake #{self.cake} by user #{self.created_by}"
 
    class Meta:
        ordering = ['created_date']
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pk': self.cake_id})
```

**Cake Model CRUD Operations**

The CRUD operations for the Cake model were my first solo responsibility after our tri-programming session was finished. I’ve chosen to highlight these features as something which struck me in programming them was how much simpler it was to construct in Django compared to my experience with Express on the previous project; the use of class-based views simplified the process almost to the point of luxury.

```py
class CakeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cake
    fields = ['name', 'flavours', 'description', 'imageurl']
    success_message = "Cake successfully created."
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
 
class CakeUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cake
    fields = ['name', 'flavours', 'description', 'imageurl']
    success_message = "Cake successfully updated."
    
class CakeDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Cake
    success_message = "Cake successfully deleted."
    success_url = '/cakes/'
```

**Recipe Pagination**

Pagination was an entirely new concept to me as of this project; as daunting as the prospect of trying to learn something unfamiliar in a new framework was, I was pleasantly surprised to find that Django’s documentation covered everything I needed to know about its implementation.

I have specifically highlighted the `CakeDetail` view and **cake_detail.html** template for this example, as these are where we wanted to have our recipes paginated while also keeping the rest of the cake’s details visible, regardless of which page of recipes is being viewed.

```py
# views.py

class CakeDetail(DetailView):
    model = Cake
    def get_context_data(self, **kwargs):
        context = super(CakeDetail, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(Recipe.objects.filter(cake=self.get_object()).order_by('created_date'), 3)
        context['page_obj'] = paginator.get_page(page)
        context['form'] = RecipeForm
        return context
```

```html
<!-- cake_detail.html -->

{% for recipe in page_obj %}
<div class="column is-one-third">
    <div class="card m3">
        <div class="card-image">
            <figure class="image is-square">
                <img src="{{ recipe.imageurl }}" id="cakeImage"/>
            </figure>
        </div>
        <div class="card-content">
            <h4 class="title is-4">
                {{ recipe.title }}
            </h4>
            <p><strong>Description:</strong> {{ recipe.description}}</p>
            <p><b>Ingredients:</b> {{recipe.ingredients}}</p>
            <p><b>Instructions:</b> {{recipe.instructions}}</p>
            <hr>
            <p><em>Added by {{ recipe.created_by }} on {{ recipe.created_date }}</em></p>
        </div>
        <div class="card-footer">
            {% if user.id == recipe.created_by.id %}
            <a class="card-footer-item" href="{% url 'recipes_update' recipe.id %}">Edit</a>
            <a class="card-footer-item" href="{% url 'recipes_delete' recipe.id %}">Delete</a>
            {% endif %}
        </div>
    </div>
</div>
{% endfor %}
</div>
<div class="pagination-container column">
<nav class="pagination is-centered" role="navigation" aria-label="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a class="pagination-previous" href="?page=1">&laquo; First</a>
            <a class="pagination-previous" href="?page={{ page_obj.previous_page_number }}">Previous</a>
        {% else %}
            <a class="pagination-previous" href="#">&laquo; First</a>
            <a class="pagination-previous" href="#">Previous</a>
        {% endif %}
            
        <span class="current">
            || Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }} ||
        </span>
            
        {% if page_obj.has_next %}
            <a class="pagination-next" href="?page={{ page_obj.next_page_number }}">Next</a>
            <a class="pagination-next" href="?page={{ page_obj.paginator.num_pages }}">Last &raquo;</a>
        {% else %}
        <a class="pagination-next" href="#">Next</a>
        <a class="pagination-next" href="#">Last &raquo;</a>

```

### Outcome

#### Challenges
* The first challenge I ran up against was in the pair-programming session with Richard, where we attempted to fix the issues he was having with implementing the creation operation for recipes. As mentioned in Day 1 of Development, we experienced a problem where the page to which the user was redirected upon clicking “Add Recipe” would be unable to access the ID for the cake to which the recipe was being submitted. This issue was picked up and completed the following day by Marc, though given my successes following this particular problem, I am confident that I could have found the solution myself in good time.
* A real enigma, for which I still lack understanding, was the issue present in the Recipe deletion operation. Upon clicking “Delete” and being redirected to the confirmation page, clicking either the “Confirm” or “Cancel” would be handled as “Confirm”. Even after several attempts at rewriting the logic for the “Cancel” button, checking its attributes and any other associated behaviour, it would still behave as the “Confirm” button. Out of desperate experimentation, I attempted rendering it as an anchor tag (styled as a button) linking back to the Cake Details page from which the user had come, which somehow completely fixed the problem. My best guess is that the Delete view inherently handles buttons as confirmation, but I have been unable to find any clarification on this, and it seems like it would be a tremendous flaw in the way Django behaves.
* Using a new CSS library which no member of the team had any familiarity with presented its share of difficulty. Though simple to implement and get immediate results, our experience with CSS libraries to that point had been that they required specific structuring at times in order to achieve a certain outcome, which proved to be no different for Bulma.

#### Victories
* Implementing pagination, a process entirely unfamiliar to me at that point, by doing nothing more than following Django’s documentation felt like a significant milestone in my personal development.
* Successfully leading a three-person team and managing our time such that we had all of our required functionality by the end of our third day was hugely satisfying, as well as the comfort of knowing we had an entire free day ahead of us to attend to styling and fine-tuning.
* The experience of working in a focused, enthusiastic and supportive team, each wanting the project to turn out the very best it could, was a significant victory in its own right.

#### Bugs
* Success and Error messages on the signup form are overlaid on the form itself, rather than at the top of the page.
* As we were unable to implement responsiveness for the navigation bar, the site itself is not fully responsive.

#### Future Inclusions and Improvements
* Ideally, I would like to implement a dropdown selection on the cake index which would allow users to filter cakes by flavour profile.
* We had wanted to include a “Full Details” button for the recipe cards on each cake details page, which would display all information for that recipe in a modal view. This was because we realised that the recipe cards got quite lengthy once fully populated, and confining the bare essentials to the card itself would save a great deal of space. This feature was started, but we ran short of time before it could be fully implemented.
* We had explored the feasibility of including enhanced authentication features, such as a verification email upon registration and emailed password reset confirmations, and found that Django’s documentation appeared straightforward in doing so – unfortunately, again, we lacked the time to attempt them.



#### Key Learnings
The most significant takeaway of this project was, without a doubt, the importance of documentation. While I had attempted to do so in my previous project, Express had proven a little too unfathomable for me to implement much of what I found. This time around, I found myself far more capable of extracting salient information from the documentation and putting it into practice.
The other major lesson I gleaned from my experience was the significance of thorough, evenly-contributed input from the team. Though Richard had been experiencing more difficulty with Python and Django concepts than myself and Marc, he consistently demonstrated his willingness to attempt solving problems and was always willing to provide support to the best of his ability. It was refreshing, and eye-opening, to be part of a team where each member was willing to support one another regardless of their understanding or progress, and has inspired me to try and foster that same environment and atmosphere in any team I might be part of in future.
