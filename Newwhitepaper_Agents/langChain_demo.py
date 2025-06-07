from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.tools import GooglePlacesTool
import os
from langchain_google_vertexai import ChatVertexAI

os.environ["SERPAPI_API_KEY"] = "your key"
os.environ["GPLACES_API_KEY"] = "your key"
@tool
def search(query: str):
    """Use the SerpAPI to run a Google Search."""
    search = SerpAPIWrapper()
    return search.run(query)

@tool
def places(query: str):
    """Use the Google Places API to run a Google Places Query."""
    places = GooglePlacesTool()
    return places.run(query)

model = ChatVertexAI(model="gemini-2.0-flash-001") # this changed to new model version, old expired
tools = [search, places]

query = "Who did the Texas Longhorns play in football last week? What is the address of the other team's stadium?"
agent = create_react_agent(model, tools)
input = {"messages": [("human", query)]}
for s in agent.stream(input, stream_mode="values"):
    message = s["messages"][-1]
    if isinstance(message, tuple):
        print(message)
    else:
        message.pretty_print()

# debug logs:
# case1:
# ================================ Human Message =================================

# Who did the Texas Longhorns play in football last week? What is the address of the other team's stadium?
# ================================== Ai Message ==================================
# Tool Calls:
#   search (xxx)
#  Call ID: xxx
#   Args:
#     query: who did the Texas Longhorns play last week in football?
# ================================= Tool Message =================================
# Name: search

# ['Visit ESPN for Texas Longhorns live scores, video highlights, and latest news. Find standings and the full 2025 season schedule.', 'Texas Longhorns Schedule 2025 ; Sat, 9/13. vs UTEP · 1:15 PM ; Sat, 9/20. vs SHSU · TBD ; Sat, 10/4. @ FLA · TBD ; Sat, 10/11. vs OU *. 12:30 PM ; Sat, 10/18. @ UK.', 'GAME LOG ; 1/10 · vs · Ohio State · 6. Ohio State.', 'The official Football page for the University of Texas Longhorns.', 'Atwood, Kavan power No. 6 Texas past No. 12 Texas Tech June 04, 2025. Reese Atwood hits a single to bring in the winning runs for the Longhorns as Teagan ...', 'Get the latest news and information for the Texas Longhorns. 2025 season schedule, scores, stats, and highlights. Find out the latest on your favorite NCAAF ...', 'After two different replay reviews towards the end of the matchup against Texas Tech, Kavan reflects on how the Longhorns came together to get the last out for ...', 'Scheduled Games · Ohio State University Logo. Aug 30 (Sat) 11 a.m. · San Jose State University Logo. Sep 6 (Sat) 11 a.m. · University of Texas-El Paso Logo · Sam ...', 'Texas Longhorns ; Sep 13, 2025, vs. team logo · UTEP · 4:15 pm ; Sep 20, 2025, vs. team logo · Sam Houston · 8:00 pm ; Oct 4, 2025, @. team logo · Florida · TBA.', 'Full 2025-26 Texas Longhorns schedule. Scores, opponents, and dates of games for the entire season.']
# ================================== Ai Message ==================================

# The Texas Longhorns played UTEP on September 13, 2025, and Sam Houston on September 20, 2025. To find the address of the UTEP stadium, I will run another search.
# Tool Calls:
#   search (xxx)
#  Call ID: xxx
#   Args:
#     query: address of UTEP stadium
# ================================= Tool Message =================================
# Name: search

# ['The Sun Bowl is an outdoor football stadium in the Southwestern United States, on the campus of the University of Texas at El Paso. It is home to the UTEP Miners of Conference USA, and the late December college football bowl game, the Sun Bowl.', 'Sun Bowl type: Stadium in El Paso, Texas.', 'Sun Bowl entity_type: local_nav.', 'Sun Bowl kgmid: /m/03092m.', 'Sun Bowl place_id: ChIJJ3x541xY54YRSMj0HkXCzrA.', 'Sun Bowl located_in: University of Texas at El Paso.', 'Sun Bowl address: 2701 Sun Bowl Dr, El Paso, TX 79902.', 'Sun Bowl capacity: 51,500.', 'Sun Bowl team: UTEP Miners football.', 'Sun Bowl opened: September 21, 1963.', 'Sun Bowl elevation: 3,910 feet (1,190 m).', 'Sun Bowl renovated: 2006, 2018.', 'Sun Bowl surface: Natural grass (1963–1973); AstroTurf (1974–2000); AstroPlay (2001–2014); FieldTurf (2015–present).', 'Sun Bowl construction_cost: $275,000; (approximate, original).', 'Sun Bowl architect: Garland & Hilles; Carroll & Daeuble.', 'Sun Bowl coordinates: 31°46′23″N 106°30′29″W\ufeff / \ufeff31.773°N 106.508°W.', 'Sun Bowl broke_ground: August 1, 1961; 63 years ago.', '2701 Sun Bowl Dr, El Paso, TX 79902 · Bowl Seating: 46,098 seats including 120 wheelchair spaces. · Approx. 7,900 parking spaces surrounding the Sun Bowl · Sun ...', '... location of the stadium. It is literally in the Franklin Mountain, with a great view of El Paso and Juarez. Parking for events has improved with all the new ...', 'Sun Bowl Stadium. Address: 2501 Sun Bowl Drive - UTEP Campus, El Paso, TX 79902 ... VIEW ALL SUN BOWL STADIUM EVENTS. Union Cinema. Address: 500 W. Universtiy ...', 'Get more information for Sun Bowl in El Paso, TX. See reviews, map, get the address, and find directions.', 'UTEP Sun Bowl Stadium, El Paso, Texas. 5540 likes · 149 talking about this · 96373 were here. Football Stadium.', 'The stadium is not only home to the UTEP football team, but also houses the Sun Bowl game every December. Recent additions to the stadium have included a state- ...', 'Address: 151 Glory Rd, El Paso, TX 79902. Your browser does not support ... SUN BOWL STADIUM SEATING CHART AND CAPACITY. Driving Directions to Sun Bowl ...', "MAP & DIRECTIONS TO THE STADIUM. Address: Sun Bowl Drive, El Paso, TX 79968. View Larger Map | Get Directions | View Bird's Eye. FROM: Address or Intersection: ...", '6701 Convair Rd El Paso, Texas 79925. 915-534-0600. Monday - Friday 8AM - 5PM Saturday - Sunday 8AM - 2PM. Jobs Staff Media Gallery Resources · Privacy Policy ...', 'Sun Bowl Stadium is located at 2701 Sun Bowl Drive, El Paso, TX. What can I bring into Sun Bowl Stadium? While exact rules vary from venue to venue, there are ...']
# ================================== Ai Message ==================================

# The UTEP stadium, called the Sun Bowl, is located at 2701 Sun Bowl Dr, El Paso, TX 79902.



# -----------------------------------------
# case2:
# ================================ Human Message =================================

# Who did the Texas Longhorns play in football last week? What is the address of the other team's stadium?
# ================================== Ai Message ==================================
# Tool Calls:
#   search (xxx)
#  Call ID: xxx
#   Args:
#     query: who did the Texas Longhorns play last week football
# ================================= Tool Message =================================
# Name: search

# ['Visit ESPN for Texas Longhorns live scores, video highlights, and latest news. Find standings and the full 2025 season schedule.', 'Texas Longhorns Schedule 2025 ; Sat, 9/13. vs UTEP · 1:15 PM ; Sat, 9/20. vs SHSU · TBD ; Sat, 10/4. @ FLA · TBD ; Sat, 10/11. vs OU *. 12:30 PM ; Sat, 10/18. @ UK.', 'GAME LOG ; 1/10 · vs · Ohio State · 6. Ohio State.', 'The official Football page for the University of Texas Longhorns.', 'Atwood, Kavan power No. 6 Texas past No. 12 Texas Tech June 04, 2025. Reese Atwood hits a single to bring in the winning runs for the Longhorns as Teagan ...', 'Get the latest news and information for the Texas Longhorns. 2025 season schedule, scores, stats, and highlights. Find out the latest on your favorite NCAAF ...', 'Texas Longhorns previous match was against Ohio State Buckeyes in NCAA Division I, FBS Post Season, match ended with result 14 - 28 (Ohio State Buckeyes won the ...', 'After two different replay reviews towards the end of the matchup against Texas Tech, Kavan reflects on how the Longhorns came together to get the last out for ...', 'Scheduled Games · Ohio State University Logo. Aug 30 (Sat) 11 a.m. · San Jose State University Logo. Sep 6 (Sat) 11 a.m. · University of Texas-El Paso Logo · Sam ...', 'Full 2025-26 Texas Longhorns schedule. Scores, opponents, and dates of games for the entire season.']
# ================================== Ai Message ==================================

# The Texas Longhorns played Ohio State on January 10.
# Tool Calls:
#   places (xxx)
#  Call ID: xxx
#   Args:
#     query: Ohio State Buckeyes stadium address
# ================================= Tool Message =================================
# Name: places

# Google Places did not find any places that match the description
# ================================== Ai Message ==================================

# I was unable to find the address of the Ohio State Buckeyes stadium. I will try a different query.
# Tool Calls:
#   search (xxx)
#  Call ID: xxx
#   Args:
#     query: Ohio State Buckeyes stadium address
# ================================= Tool Message =================================
# Name: search

# ["Ohio Stadium is an American football stadium in Columbus, Ohio, on the campus of Ohio State University. It primarily serves as the home venue of the Ohio State Buckeyes football team and is also the site for the university's Spring Commencement ceremonies each May.", 'Ohio Stadium type: Stadium in Columbus, Ohio.', 'Ohio Stadium entity_type: local_nav.', 'Ohio Stadium kgmid: /m/03bt01.', 'Ohio Stadium place_id: ChIJVX_yAZSOOIgRpZhJFs2DSUs.', 'Ohio Stadium address: 411 Woody Hayes Dr, Columbus, OH 43210.', 'Ohio Stadium capacity: 102,780.', 'Ohio Stadium height: 166′.', 'Ohio Stadium area: 10 acres.', 'Ohio Stadium team: Ohio State Buckeyes football.', 'Ohio Stadium nickname: The Horseshoe yahoo.com.', 'Ohio Stadium opened: October 7, 1922.', 'Ohio Stadium construction_cost: US$1.34 million; ($25.2 million in 2024 dollars).', 'Ohio Stadium renovated: 2000–01.', 'Ohio Stadium architect: Howard Dwight Smith; Class of 1907.', 'Ohio Stadium expanded: 1948, 1991, 2001, 2014.', 'Ohio Stadium owner: Ohio State University.', 'Ohio Stadium coordinates: 40°0′6″N 83°1′11″W\ufeff / \ufeff40.00167°N 83.01972°W.', 'Ohio Stadium phone: (800) 462-8257.', 'The stadium is located toward the eastern side of campus and is only an eight minute drive from downtown Columbus, OH. Known for its double-deck horseshoe ...', '411 Woody Hayes Dr, Columbus, Ohio, United States. Open in Waze. 614-292-6330 · ohiostatebuckeyes.com/facilities/ohio-stadium.html. Onsite services.', 'Ohio Stadium is an American football stadium in Columbus, Ohio, on the campus of Ohio State University.', '411 Woody Hayes Dr Columbus, OH 43210 · (614) 292-2661.', 'Watching the Buckeyes play football here is wonderful. A night game is magical. Pretty easy in and out. Food is not crazy expensive. Lots of good seats.', '1. Ohio Stadium, 411 Woody Hayes Drive · 2. 131 St. John Arena, 410 Woody Hayes Drive · 3. 102 Athletics Maintenance Bldg, 2450 Fred Taylor Drive', 'Nestled snugly on the banks of the Olentangy River, stately Ohio Stadium is one of the most recognizable landmarks in all of college athletics.', 'View details about Ohio Stadium in Columbus, OH United States on Apple Maps. Address, driving directions, images, nearby attractions and more.', '411 Woody Hayes Dr. Columbus, OH 43210. Email: scarletandgrayvenues@osu.edu. Phone: 614-247-1739 ...']
# ================================== Ai Message ==================================

# The address of Ohio Stadium, where the Ohio State Buckeyes play, is 411 Woody Hayes Dr, Columbus, OH 43210.