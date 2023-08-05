import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
import sklearn

dataset = pd.read_csv('FullDataset_Laptop.csv')
dataset.drop_duplicates(subset=['name of laptop'], inplace=True)


pipe = pickle.load(open('predictpipe.pkl','rb'))
df = pickle.load(open('predictdf.pkl','rb'))


# Function to filter laptops based on user's desired price range
def filter_laptops_by_price_range(data, min_price, max_price):
    filtered_laptops = data[(data['price'] >= min_price) & (data['price'] <= max_price)]
    return filtered_laptops


# Function to get top N laptops based on maximum views
def get_top_n_laptops_by_views(data, n):
    sorted_laptops = data.sort_values(by='rating numbers', ascending=False)
    top_n_laptops = sorted_laptops.head(n)
    return top_n_laptops


st.markdown(
    """
    <style>
    .laptop-img {
        border: 1px solid #ddd;
        padding: 15px;
        border-radius: 5px;
        max-width: 300px;
    }
    .laptop-container {
        display: flex;
        align-items: center;
    }
    .laptop-info {
        margin-left: 20px;
    }
    .laptop-name {
        font-size: 1px;
        font-weight: bold;
    }
    .laptop-rating {
        font-size: 16px;
        font-weight: bold;
        color: #1e88e5;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .laptop-link a {
        color: white;
        text-decoration: none;
        font-size:18px;
        
    }
    .laptop-link a:hover {
        color: #66a3ff;
    }
    .price {
 font-size: 20px;
color: #FFFFFF;
font-weight: bold;
text-align: center;

padding: 5px;
margin: 2px;
border: 1px solid #007BFF;
border-radius: 10px;
 max-width: 300px; /* Limit the width of the price box */

}
    </style>
    """,
    unsafe_allow_html=True
)
def display_laptops(brand):
    st.write(f"Laptops of {brand} brand:")

    brand_lower = brand.lower()
    # Filter laptops based on the selected brand
    laptops_of_selected_brand = dataset[(dataset['brand'].str.lower() == brand_lower)]
    if not laptops_of_selected_brand.empty:


        for index, row in laptops_of_selected_brand.iterrows():
                flipart_png="https://www.freepnglogos.com/uploads/flipkart-logo-png/flipkart-logo-transparent-png-download-0.png"
                n = row["name of laptop"]
                st.markdown(
                    f'<div class="laptop-img-container">'
                    f'<div class="laptop-link"><a href="{row["url laptop"]}" target="_blank"><b>{n}</b>'
                    f'<img src="{flipart_png}" alt="{n} Image" style="width: 30px; height: 30px; margin-left: 5px;">'
                    f'</a></div>'
                    
                    f'<img src="{row["image-link"]}" class="laptop-img">'
                    f'<p> {row["ratings"]}⭐        Total ratings: {row["rating numbers"]}</p>'
                    f"<p class='price'>Rs {row['price']}</p>"
    
                    '</div>',
                    unsafe_allow_html=True
                )
    else:
        st.warning("sorry,Not Available  :(")
def main():



    page_options = ['Home', 'Price Predictor']
    selected_page = st.sidebar.selectbox('Navigate to:', page_options)




    if selected_page == 'Home':

        colIm, coltit = st.columns([1, 3])
        colIm.image("laptop.png", width=160)
        coltit.title("LaptopHunt: Unveiling your Perfect laptop")
        st.markdown(
            "Made by Animesh | [Portfolio](https://animesh11portfolio.streamlit.app/) | [LinkedIn](https://www.linkedin.com/in/animesh-singh11)")

        st.sidebar.title("About this page")
        st.sidebar.write("Discover your ideal laptop effortlessly with Laptops Filter! Browse through 800+ laptops from top brands and filter by brand name and price range. Make informed decisions with sentiment analysis on customer reviews. Find the perfect laptop for you at Laptops Filter - Where Your Perfect Laptop Awaits!")
        st.sidebar.write("--  Animesh")

        st.sidebar.markdown(
            "||  [cinema_nexus ](https://cinemanexus.streamlit.app/) ||   [spambuster_ai ∙](https://spambusterai.streamlit.app/)")
        st.sidebar.markdown(
            "||  [intelligence_books_suggester_app ∙](https://intelligencebookssuggesterapp.streamlit.app/)  ||")
        st.sidebar.markdown(
            "||  [youtube_video_sentimentsAnalysis..app∙](https://youtubevideosentimentanalysis.streamlit.app/)  ||")

        unique_brands = dataset['brand'].unique()
        user_brand_name = st.selectbox('Select a brand name:', unique_brands)

        price_options = [20000, 30000, 40000,50000,60000,70000,80000,90000,100000,110000]
        user_price_range = st.select_slider('Select a price range:', options=price_options)

        # Filter laptops based on the user's desired price range and selected brand
        filtered_laptops = dataset[
            (dataset['price'] <= user_price_range) &
            (dataset['name of laptop'].str.contains(user_brand_name, case=False))
        ]

        top_5_laptops = get_top_n_laptops_by_views(filtered_laptops, 10)

        st.markdown(
            """
            <style>
            .laptop-img {
                border: 1px solid #ddd;
                padding: 15px;
                border-radius: 5px;
                max-width: 300px;
            }
            .laptop-container {
                display: flex;
                align-items: center;
            }
            .laptop-info {
                margin-left: 20px;
            }
            .laptop-name {
                font-size: 15px;
                font-weight: bold;
            }
            .laptop-rating {
                font-size: 16px;
                font-weight: bold;
                color: #1e88e5;
            }
    
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <style>
            .laptop-link a {
                color: white;
                text-decoration: none;
                font-size:28px;
            }
            .laptop-link a:hover {
                color: #66a3ff;
            }
            .price {
         font-size: 40px;
        color: #FFFFFF;
        font-weight: bold;
        text-align: center;
    
        padding: 2px;
        margin: 2px;
        border: 1px solid #007BFF;
        border-radius: 10px;
         max-width: 300px; /* Limit the width of the price box */
    
        }
            </style>
            """,
            unsafe_allow_html=True
        )


        if not top_5_laptops.empty:
            st.header('')
            for index, row in top_5_laptops.iterrows():
                col1, col2 = st.columns(2)
                with col1:

                    st.markdown(
                        f'<div class="laptop-img-container">'
                        f'<img src="{row["image-link"]}" class="laptop-img">'
                        f'<p> {row["ratings"]}⭐        Total ratings: {row["rating numbers"]}</p>'
                        f"<p class='price'>Rs {row['price']}</p>"
    
                        '</div>',
                        unsafe_allow_html=True
                    )


                with col2:
                    flipart_png = "https://www.freepnglogos.com/uploads/flipkart-logo-png/flipkart-logo-transparent-png-download-0.png"

                    n=row["name of laptop"]
                    parts = n.split("-", 1)
                    desired_part = parts[0].strip()

                    laptop_name = f'<div class="laptop-link"><a href="{row["url laptop"]}" target="_blank"><b>{desired_part}</b>' \
                                  f'<img src="{flipart_png}" alt="{n} Image" style="width: 50px; height: 50px; margin-left: 5px;">'\
                                  f'</a></div>'
                    st.markdown(laptop_name, unsafe_allow_html=True)
                    st.markdown(f"->{row['processor name']}",unsafe_allow_html=True)
                    st.markdown(f"->{row['RAM']}",unsafe_allow_html=True)
                    st.markdown(f"->{row['ssd']}", unsafe_allow_html=True)
                    st.markdown(f"->{row['display']}", unsafe_allow_html=True)
                    sentiment_score = row['Sentiment Scores']

                    # Convert the sentiment score to a percentage
                    positivity_percentage = sentiment_score * 100
                    negativity_percentage = 100 - positivity_percentage

                    plt.style.use('dark_background')
                    # Plot the pie chart
                    labels = ['Positive', 'Neutral/Negative']
                    sizes = [positivity_percentage, negativity_percentage]
                    colors = ['#00adb5', '#ff6b6b']

                    # Explode the Positive slice to make it stand out
                    explode = (0.15, 0)

                    # Plot the pie chart with a black background and other customizations

                    plt.figure(figsize=(8, 6),facecolor='none', edgecolor='none')
                    plt.style.use('dark_background')

                    plt.pie(sizes, explode=explode,  colors=colors, autopct='%1.1f%%', shadow=True,
                            startangle=140,  textprops={'color': 'white', 'fontsize': 14})
                    # plt.axis('equal')


                    # Set text color to white and pie chart edgecolor to black
                    plt.rcParams['text.color'] = '#ffffff'
                    for wedge in plt.gca().patches:
                        wedge.set_edgecolor('black')
                    texts = plt.gca().texts
                    fontsize = 20  # Set the desired font size
                    for text in texts:
                        text.set_fontsize(fontsize)
                    # Set the title and legend
                    plt.title('Sentiment Distribution of Reviews', color='white', fontsize=20)
                    plt.legend(labels, loc='upper right', bbox_to_anchor=(1.3, 1), fontsize=18)

                    # Add a shadow to the pie chart
                    # plt.gca().add_artist(plt.Circle((0, 0), 0.5, color='black', fill=False))

                    # Remove the black wedge between the slices
                    plt.gca().patches[1].set_visible(False)

                    st.pyplot(plt)

                st.markdown('---')  # Add a horizontal rule after each laptop

        else:
            st.warning('No laptops found within the specified price range for the selected laptop name.')

    elif selected_page == 'Price Predictor':
        st.subheader("SmartLapPrix: Unlock Laptop Prices, Unleash Savings....💻💸 ")
        st.sidebar.title("About this Page")
        st.sidebar.write("Welcome ! This web app is designed to predict laptop prices with an impressive accuracy of 90%. With your selections, It provide personalized price estimates and recommend updated laptops that match your preferences. Shop smart and confidently with Laptop Price Predictor by your side..")
        st.sidebar.write("-- Animesh")

        company = st.selectbox('Brand', df['Company'].unique())

        # type of laptop
        type = st.selectbox('Type', df['TypeName'].unique())

        ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
        weight = st.slider('Select Weight', min_value=1.0, max_value=3.0, step=0.01)
        touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
        ips = st.selectbox('IPS', ['No', 'Yes'])

        screen_size = st.slider('Select Screen Size', min_value=10.0, max_value=18.0, step=0.1)

        # screen size
        # screen_size = st.number_input('Screen Size')

        # resolution
        resolution = st.selectbox('Screen Resolution',
                                  ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800',
                                   '2560x1600', '2560x1440', '2304x1440'])

        # cpu
        cpu = st.selectbox('CPU', df['Cpu brand'].unique())

        hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

        ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

        gpu = st.selectbox('GPU', df['Gpu brand'].unique())

        os = st.selectbox('OS', df['os'].unique())

        if st.button('Predict Price'):
            # query
            ppi = None
            if touchscreen == 'Yes':
                touchscreen = 1
            else:
                touchscreen = 0

            if ips == 'Yes':
                ips = 1
            else:
                ips = 0

            X_res = int(resolution.split('x')[0])
            Y_res = int(resolution.split('x')[1])
            ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size
            query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

            query = query.reshape(1, 12)
            st.success("umm ig price should be : " + str(int(np.exp(pipe.predict(query)[0]))))

            display_laptops(company)

        # Note: Replace 'path_to_model.pkl' and 'path_to_dataframe.csv' wit

if __name__ == "__main__":
    main()



