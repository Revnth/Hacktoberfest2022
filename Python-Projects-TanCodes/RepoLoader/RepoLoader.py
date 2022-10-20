from altair.vegalite.v4.schema.channels import Column
import streamlit as st
from bs4 import BeautifulSoup
import pandas as pd
import requests
from annotated_text import annotated_text
from PIL import Image
import base64
import time
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="RepoLoader")

# Creating 3 columns
col1, col2, col3 = st.columns([2, 8, 2])

# > COLUMN 1 - Empty
with col1:
    st.write("")

# > COLUMN 2
with col2:
    # RepoLoader  Logo
    image = Image.open("logo.png")
    st.image(image)

    # Username and Load Button
    USERNAME = st.text_input("Enter Github username", "")
    load_button = st.button("Load Repo 🔽")

    if load_button:

        # ! IF INPUT FIELD IS EMPTY SHOW ERROR
        if not USERNAME or '/' in USERNAME or '?' in USERNAME:
            st.markdown(
                "<h4 style='text-align: center; color:#FF4848;'>  Invalid username </h4>",
                unsafe_allow_html=True,
            )

        # > ELSE SHOW THIS
        else:
            with st.spinner("Repo Loading..."):
                time.sleep(2)
                st.success("Repo loaded successfully!")

            base_url = "https://github.com"
            url = f"{base_url}/{USERNAME}?tab=repositories"

            # API DATA
            link = f"https://api.github.com/users/{USERNAME}/repos?per_page=1000"
            api_link = requests.get(link)
            api_data = api_link.json()

            get_url = requests.get(url)

            # ^ IF success status 200 OK
            if get_url.status_code == 200:

                data = BeautifulSoup(get_url.text, "html.parser")

                # name of the Repo owner
                name_class = data.find_all(class_="p-name")
                for tag in name_class:
                    NAME = tag.text.strip()

                # total number of repo
                repo_class = data.find(class_="Counter")
                TOTAL_REPO = repo_class.text
                to_compare = int(TOTAL_REPO)

                # IF REPO SIZE IS = 0 THAT MEANS IT IS AN EMPTY REPO
                if to_compare == 0:
                    st.error("This Repository is empty")

                else:
                    annotated_text(
                        "Name of the owner : ",
                        (f"{NAME}", "", "#afa"),
                        (" ", " "),
                        "Total number of repos : ",
                        (f"{TOTAL_REPO}", "", "#afa"),
                    )
                    st.text("")

                    repos_name = []
                    repos_link = []
                    repos_language = []
                    repos_fork = []
                    repos_date = []

                    # Repo table
                    for items in api_data:
                        repos_name.append(items["name"])

                        item_link = items["svn_url"]
                        repos_link.append(item_link)

                        repos_language.append(items["language"])
                        final_language = [
                            "unknown" if i == None else i for i in repos_language
                        ]

                        repos_fork.append(items["fork"])
                        final_fork = [
                            "✅" if i == True else "❌" if i == False else 0
                            for i in repos_fork
                        ]

                        item_date = items["updated_at"][:10]
                        repos_date.append(item_date)

                    temp = list(
                        zip(
                            repos_name,
                            repos_link,
                            final_language,
                            final_fork,
                            repos_date,
                        )
                    )

                    # Number of is forked repo
                    is_forked_count = final_fork.count("✅")

                    df = pd.DataFrame(
                        temp,
                        columns=[
                            "Project Name",
                            "Project Link",
                            "Main Language",
                            f"Is Forked? ({is_forked_count})",
                            "Date",
                        ],
                    )  # Dataframe

                    TABLE_REPO = df.sort_values(by="Date", ascending=False).reset_index(
                        drop=True
                    )  # Sort by dates

                    Final_data = st.dataframe(TABLE_REPO)

                    #  ALERT MESSAGE
                    if to_compare > 100:
                        st.warning("Only displays the first 100 updated Repos")
                    else:
                        message = ""

                    # TO GET THE DATA AND MAKE IT AS A CSV FILE
                    coded_data = base64.b64encode(
                        TABLE_REPO.to_csv(index=False).encode()
                    ).decode()
                    st.markdown(
                        f'<a href="data:file/csv;base64,{coded_data}" download="{USERNAME}.csv"> **Download {USERNAME} Data**</a> 📥 ',
                        unsafe_allow_html=True,
                    )

                    # PIE CHART
                    counts = TABLE_REPO["Main Language"].value_counts()
                    language_names = counts.index
                    language_values = counts.values

                    fig = go.Figure(
                        go.Pie(
                            title=f"PIE CHART : Most languages used by {NAME}",
                            labels=language_names,
                            values=language_values,
                            hoverinfo="label+percent",
                            textinfo="value",
                        )
                    )

                    st.plotly_chart(fig, use_container_width=True)

            #! ELSE PRINT ERROR FOR STATUS CODE 404
            else:
                print(get_url.status_code)
                st.markdown(
                    "<h4 style='text-align: center; color:#FF4848;'>  Username Not exist  </h4>",
                    unsafe_allow_html=True,
                )

    st.markdown("""---""")

    # > This for ABOUT - HOW TO USE  - DEVELOPER.
    expander = st.expander("📖 ABOUT ")
    expander.markdown(
        """
                   _________

                   # 📖 ABOUT
                   _________
                   
                   RepoLoader is for the developers who are constantly visiting Github which will make their work a little bit easy. It will save the developers 
                   time to visit GitHub and search the username of the particular repo and changing tabs and all this stuff so We have made the work simpler. 
                   Just search the username and you will get only what the user want.  Yeah, only Repos. 

                   ## 🔧 Features

                   - User can also download the repo dataset in CSV so that user can also use it for analysis, etc.
                   - NO need of opening GitHub and searching for the repos.
                   - Gives the name of the owner and the number of repositories is there in that.
                   - Shows only Repos name , with the last updated date and with the project links.
                  
        """
    )

    expander = st.expander("💡 HOW TO USE")
    expander.markdown(
        """
                   _________
                   # 💡 HOW TO USE
                   _________
                    
                   #### 1-> Enter the GitHub username and then click "Load Repo" button.
                    
                    ![](https://ik.imagekit.io/tfme5aczhhf/repoloader/tr:w-700/p1_TN37GSg7G.PNG?updatedAt=1633793484426)

                   #### 2-> This is what the user will get the output. 

                    ![](https://ik.imagekit.io/tfme5aczhhf/repoloader/tr:w-700/p2_Z4SMxmovL.PNG)

                    User can also download this data for further use.
                    ![](https://ik.imagekit.io/tfme5aczhhf/repoloader/tr:w-750/p3_ZgYGowiBx.PNG)

        """
    )

    expander = st.expander("📌 ABOUT DEVELOPER")
    expander.markdown(
        """
            
                    _________
                    ## Find me around the web 🌎:
                    
                    💻 [Portfolio](http://tancodes.atspace.cc/)
                    📌 [GitHub](https://github.com/TanCodes)
                    💼 [LinkedIN](https://www.linkedin.com/in/tanmay-barvi-2a0206126/)
                    🎬 [YouTube](https://www.youtube.com/channel/UC370GTtJnvWs8wDH9UXoBzQ?view_as=subscriber)
                    ❤️ [Instagram](https://instagram.com/_tancodes_)
                    🐦 [Twitter](https://twitter.com/_tancodes_)
                    _________
                
                    ###  HAPPY CODING WITH PYTHON 
                    ![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
                    ![forthebadge](https://camo.githubusercontent.com/5e18e9b742657f6921829e31b6ee09d5d345633d8680cf1881f637d8e7bc44f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50616e6461732d3243324437323f7374796c653d666f722d7468652d6261646765266c6f676f3d70616e646173266c6f676f436f6c6f723d7768697465)
                    ![](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
                    ![forthebadge](https://camo.githubusercontent.com/19899a4404e48401369f8bc3d262705dc9259348b5323fca27d2717fab2f1b00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5765622532307363726170696e672d626c61636b3f7374796c653d666f722d7468652d6261646765266c6f676f3d6170707665796f72)
                    ![](https://forthebadge.com/images/badges/built-with-love.svg)
                    _________
        """
    )

# > COLUMN 3 - Empty
with col3:

    st.markdown("""[  👨‍💻](https://github.com/TanCodes/RepoLoader "Get Code") """)

# > Removing footer and main menu from default streamlit
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
