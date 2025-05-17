import os
import django

# Set environment variable and setup Django before using ORM
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # adjust if different
django.setup()

from django.contrib.auth.models import User
from ..campaign.models import BlogPost  # replace with your actual app and model name
from django.utils.text import slugify
from django.utils import timezone

author = User.objects.first()  # Assumes a user already exists

posts = [
    {
        "title": "Why Community Engagement Matters in Campaigns",
        "excerpt": "Learn why connecting with your local community is essential for a successful political campaign.",
        "content": """Community engagement is not just a buzzword—it’s the foundation of any impactful political campaign. When candidates take the time to listen to the voices of the people they hope to represent, they demonstrate authenticity and commitment to democratic values. Community forums, door-to-door canvassing, local town halls, and social media engagement all play critical roles in shaping a two-way dialogue between citizens and campaign teams. These platforms allow residents to express concerns, provide feedback, and contribute ideas that help shape policy priorities. Furthermore, when people feel heard, they are more likely to vote, volunteer, and become advocates for your platform. Engaging with the community also allows campaigns to better tailor their messaging to address local needs and build meaningful coalitions. The most successful movements are those built from the ground up, rooted in the daily realities of real people. Ultimately, community engagement transforms campaigns from a top-down directive into a collective movement driven by shared values and goals.""",
    },
    {
        "title": "5 Key Policies We’re Fighting For",
        "excerpt": "Here are the five critical issues our campaign is focused on solving for you.",
        "content": """Our campaign is built around five key policy pillars that we believe are crucial for the progress and prosperity of our community. First, we are committed to healthcare reform that ensures affordable and accessible care for all, especially vulnerable and rural populations. Second, we advocate for comprehensive education funding to improve infrastructure, teacher training, and access to technology. Third, we support sustainable economic development with a focus on local entrepreneurship, job creation, and fair wages. Fourth, we prioritize climate action, with plans to promote clean energy, invest in green jobs, and implement environmental protection measures. Finally, we are working toward social justice and equity, including criminal justice reform, gender equality, and the protection of minority rights. These policies are not abstract ideas—they are grounded in data, shaped by community feedback, and informed by what’s already working elsewhere. Together, these pillars form the backbone of our vision for a better, fairer society.""",
    },
    {
        "title": "Behind the Scenes: A Day on the Trail",
        "excerpt": "Go behind the curtain to see the daily grind and inspiration fueling our campaign journey.",
        "content": """The campaign trail is both exhilarating and exhausting. Each day starts early, often before sunrise, with strategy meetings over coffee to review the day's schedule, media briefings, and key talking points. The candidate then heads to local venues—schools, businesses, and community centers—to meet voters face-to-face. Each handshake and conversation offers insights into what really matters to people. Between events, the team works tirelessly to coordinate logistics, update social media channels, and handle press inquiries. Volunteers distribute flyers, make phone calls, and mobilize local support. The afternoons are usually packed with interviews, live panels, and town halls. Evenings are reserved for fundraisers and community dinners where authentic connections are forged over shared meals and stories. Behind every campaign event is a dedicated crew managing sound checks, signage, and crowd control. There’s a rhythm to the chaos, a shared sense of purpose that keeps everyone motivated. Despite the physical toll, the energy of the people fuels us. Every challenge encountered on the trail becomes a lesson that refines our message and deepens our resolve to serve. The work is relentless, but every moment is a step toward meaningful change.""",
    },
    {
        "title": "Meet Our Campaign Team",
        "excerpt": "Get to know the dedicated people working tirelessly to bring change to your community.",
        "content": """A campaign is only as strong as the team behind it. While the candidate often takes the spotlight, the daily work of organizing events, developing policies, and engaging the public falls on the shoulders of a diverse, skilled, and passionate group of individuals. Our campaign manager ensures that timelines are met and goals are exceeded. The communications team crafts messages, handles media relations, and maintains our online presence across multiple platforms. Policy advisors spend long hours researching legislation, analyzing community data, and drafting practical proposals that reflect the needs of our constituents. Field organizers coordinate outreach efforts, connecting volunteers with voters across neighborhoods. Our finance team tracks donations, ensures transparency, and manages budgets to keep the campaign sustainable. Then there are the tireless volunteers who phone bank, canvass door-to-door, and create a welcoming presence at every campaign event. Each member plays a crucial role in shaping the movement. What unites us is not just a shared professional commitment, but a deep belief in the mission we serve: to bring about inclusive, data-informed, and community-driven change.""",
    },
    {
        "title": "How You Can Make a Difference",
        "excerpt": "Want to help? Here's how you can support our movement for a better future.",
        "content": """Political change begins with the people, and your involvement can make a significant difference. Whether you're a seasoned organizer or someone just beginning to engage in civic life, there are numerous ways to contribute to our campaign. First, consider volunteering your time to phone bank, knock on doors, or help with event logistics. Even a few hours each week can multiply our outreach efforts. Second, if you're active on social media, help amplify our message by sharing posts, attending virtual events, and encouraging dialogue online. Third, financial contributions, no matter how small, help us cover campaign expenses like travel, printing, and outreach materials. If you're a student or educator, organize discussions about key policy issues. If you're a community leader, host a listening session or neighborhood forum. We also need artists, photographers, designers, and tech-savvy individuals to help with creative projects. Finally, the most powerful thing you can do is vote—and encourage others to do the same. Change doesn't happen in a vacuum. It takes a coalition of committed people working toward a shared vision. Join us, and let’s build a future that reflects the hopes of our communities.""",
    },
]

for post in posts:
    BlogPost.objects.create(
        title=post["title"],
        slug=slugify(post["title"]),
        author=author,
        content=post["content"],
        excerpt=post["excerpt"],
        published_at=timezone.now(),
        is_published=True
    )



from django.utils import timezone
from datetime import timedelta

now = timezone.now()

events = [
    {
        "title": "Community Clean-Up Day",
        "description": "Join us for a day dedicated to cleaning up our local parks and streets. Bring gloves and a smile!",
        "location": "Central Park",
        "start_time": now + timedelta(days=7, hours=9),
        "end_time": now + timedelta(days=7, hours=13),
        "registration_link": "https://example.com/cleanup-signup",
    },
    {
        "title": "Youth Leadership Workshop",
        "description": "A workshop designed to empower young leaders with skills in public speaking, organizing, and advocacy.",
        "location": "City Library Conference Room",
        "start_time": now + timedelta(days=14, hours=10),
        "end_time": now + timedelta(days=14, hours=16),
        "registration_link": "https://example.com/youth-leadership",
    },
    {
        "title": "Local Candidates Forum",
        "description": "Meet the candidates running for local office and ask your questions in an open forum.",
        "location": "Community Center Auditorium",
        "start_time": now + timedelta(days=3, hours=18),
        "end_time": now + timedelta(days=3, hours=20),
        "registration_link": "",
    },
    {
        "title": "Climate Action Rally",
        "description": "Stand with us to demand urgent climate policies. Speakers, music, and community organizing.",
        "location": "Town Square",
        "start_time": now + timedelta(days=10, hours=15),
        "end_time": now + timedelta(days=10, hours=18),
        "registration_link": "https://example.com/climate-rally",
    },
    {
        "title": "Voter Registration Drive",
        "description": "Help us register voters ahead of the upcoming election. Training and materials provided.",
        "location": "Downtown Plaza",
        "start_time": now + timedelta(days=5, hours=11),
        "end_time": now + timedelta(days=5, hours=16),
        "registration_link": "https://example.com/register-to-vote",
    },
]

for event in events:
    Event.objects.create(
        title=event["title"],
        description=event["description"],
        location=event["location"],
        start_time=event["start_time"],
        end_time=event["end_time"],
        registration_link=event["registration_link"],
    )
