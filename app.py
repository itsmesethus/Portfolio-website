import streamlit as st
import os
import base64



# Set page title and favicon
st.set_page_config(page_title='Sethu S Portfolio Website ', layout='wide',initial_sidebar_state='expanded')

# Header
st.markdown("<h1 style='text-align: center; font-weight: bold;font-size: 3.2em;'>Welcome To My Data Science Portfolio Website!</h1>", unsafe_allow_html=True)
st.write('')
st.write('')
    
# Custom CSS for sidebar buttons
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        text-align: left;
        font-weight: bold;
        font-size: 40em; 
        height: 40px; /* Increase the button height */
        line-height: 40px; /* Center the text vertically */
    }
    .centered {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Navigation Bar
st.sidebar.markdown("<h2 style='font-weight: bold;' class='centered'>SECTIONS</h2>", unsafe_allow_html=True,)

# Initialize session_state
if 'section' not in st.session_state:
    st.session_state.section = 'ABOUT'

#initializing sidebar button with sections
choice_about = st.sidebar.button("**ABOUT**", key='**ABOUT**')
choice_experience = st.sidebar.button("**EXPERIENCE**", key='**EXPERIENCE**')
choice_education = st.sidebar.button("**EDUCATION**", key='**EDUCATION**')
choice_skills = st.sidebar.button("**SKILLS**", key='**SKILLS**')
choice_projects = st.sidebar.button("**PROJECTS**", key='**PROJECTS**')
choice_certifications = st.sidebar.button("**CERTIFICATIONS**", key='**CERTIFICATIONS**')
choice_contact = st.sidebar.button("**CONTACT**", key='**CONTACT**')

#session state to change section
if choice_about:
    st.session_state.section = 'ABOUT'
elif choice_experience:
    st.session_state.section = 'EXPERIENCE'
elif choice_education:
    st.session_state.section = 'EDUCATION'
elif choice_skills:
    st.session_state.section = 'SKILLS'
elif choice_projects:
    st.session_state.section = 'PROJECTS'
elif choice_certifications:
    st.session_state.section = 'CERTIFICATIONS'
elif choice_contact:
    st.session_state.section = 'CONTACT'


with st.container(border=True):
        st.write(' ')
        st.markdown(f"<h2 style='text-align: center; font-weight: bold; font-size: 3em;'>{st.session_state.section}</h2>", unsafe_allow_html=True)
        st.write(' ')
    
st.write(' ')
st.write(' ')       
st.write(' ')
st.write(' ')
st.write(' ')       
st.write(' ')
st.write(' ')
st.write(' ')       
st.write(' ')
#About section
if st.session_state.section == 'ABOUT':
    with st.container(border=True):
                    i1,i2,i3=st.columns(3)

                    with i1:
                        st.write(' ')
                    with i2:
     
                        st.markdown("""
                    <style>
                    img {
                    border-radius: 90%;
                    overflow: hidden;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 600px;  /* Set the width of the image */
                    height: 600px; /* Set the height of the image */
                    border: 7px solid #0C0C0C;s
                    }
                    </style>
                    """, unsafe_allow_html=True)
                    
                        st.image("pictures/111.png", use_column_width=True, output_format="auto")
                    with i3:
                        st.write(' ')
                
                    st.markdown("<h1 style='text-align: center; font-weight: bold;font-size: 3.5em;'>Sethu S</h1>", unsafe_allow_html=True)
                    st.markdown("<h3 style='text-align: center; font-weight: bold;font-size: 3em;'>Data Scientist | Statistician | Data Analyst </h3>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align:center; font-weight: bold;font-size: 2em;'>sethus4791@gmail.com | <a href='https://www.kaggle.com/sethu123123'>Kaggle</a> | <a href='https://github.com/itsmesethus'>GitHub</a> | <a href='https://www.linkedin.com/in/sethus4791'>LinkedIn</a> </h5>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: center; font-weight: bold;font-size: 2em;'>Villupuram, Tamil Nadu-605103 | +91-8122815260</h5>",unsafe_allow_html=True)
                    st.write('')
                    st.write('')
    #with st.container(border=True):
    r1,r2,r3=st.columns(3)
    with r1:
             st.write(' ')
    with r2:
            st.write(' ')
            #st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> Click the below button to download my Resume  :</div>""",unsafe_allow_html=True)
            resume_path = "resume/res.pdf"  # Replace with your actual resume file path
            st.download_button(label="**Download Resume**", data=open(resume_path, 'rb').read(), file_name='Sethu_S_Data_Scientist_resume.pdf', mime='application/pdf',help='Download My Resume Here!',use_container_width=True)
            st.write(' ')
    with r3:
             st.write(' ')
    # About Section Content
    with st.container(border=True):
        st.write("")
        st.markdown("""<div style='text-align: justify; font-size: 1.5em;'>  
                    Hi, I'm Sethu S, a Statistician/Data Scientist with a year of experience at Evoscien. 
I hold a Master's in Statistics from Bharathiar University, skilled in Python, R, and SQL. 
Passionate about transforming complex data into actionable insights, 
I excel in Data Cleaning, Statistical & Ml Modeling, Time Series Analysis and  Data Visualization using Matplotlib, Seaborn, Plotly, and Power BI. 
Eager to learn and grow, I stay updated with the latest data science trends through certifications and courses. 
My goal? To empower businesses with data-driven decisions and optimize processes. 
Let's collaborate and unlock the potential of your data!</div>""",unsafe_allow_html=True)
        st.write(' ')
        #st.markdown("""<div style='text-align: justify; font-size: 1.5em;'>  I'm always eager to learn and stay updated with the latest trends in data science. I keep expanding my skills through certifications and online courses to make sure I'm using the latest and greatest tools and techniques.
           # My goal is simple: to use data science to help businesses make smarter decisions, optimize their processes, and ultimately, achieve success. I'm super excited about collaborating with forward-thinking individuals and tackling complex challenges with data-driven solutions. 
        #If you're interested in leveraging the power of 
        #data to achieve your goals, I'd love to connect and explore how we can work together!</div>""",unsafe_allow_html=True)
        st.write(" ")
        st.write(' ')

    #     resume_path = "resume\Sethu_S_Data_Scientist_Resume.pdf"  # Replace with your actual resume file path
    #         st.download_button(label="**Download Resume**", data=open(resume_path, 'rb').read(), file_name='Sethu_S_Resume.pdf', mime='application/pdf',help='Download My Resume Here!',use_container_width=True)
    # with r3:





# EXPERIENCE SECTION
elif st.session_state.section == 'EXPERIENCE':
    st.write('')
    st.write('')  
    with st.container(border=True):
            st.markdown("<h2 style='text-align: center; font-weight: bold;font-size: 3em;'>Evoscien Pvt Ltd - Statistician </h2>", unsafe_allow_html=True)
            st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 10px; margin-right: 10px;'>
            <span style='text-align: left; font-weight: bold; font-size: 2em;'>Bangalore, India</span>
            <span style='text-align: right; font-weight: bold; font-size: 2em;'>May 2023 - Present</span>
            </div>
            """, unsafe_allow_html=True)
            st.write(' ')
            st.write(' ')
        #with e3:
            with st.container(border=True):
               
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 2em;font-weight:bold;'>  Description :</div>""",unsafe_allow_html=True)
                st.write('')
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Managed and preprocessed large datasets obtained from the Entomology research team, ensuring data integrity and suitability for further  statistical analysis.</div>""",unsafe_allow_html=True)
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Designed and implemented statistical models, algorithms, and techniques, extracting insights that led to a 15% improvement in decision-making processes.</div>""",unsafe_allow_html=True)
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Conducted appropriate statistical tests (t-tests, ANOVA, chi-square tests, and non-parametric tests) to analyze data and identified meaningful patterns, trends, and relationships with a 95% confidence interval.</div>""",unsafe_allow_html=True)
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Collaborated with Entomology and Engineering with data-driven approaches, resulting in improved operational efficiency by 15%.</div>""",unsafe_allow_html=True)
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Created 20+ detailed reports and interactive data visualizations, effectively communicating analytical findings to both technical and non-technical audiences.</div>""",unsafe_allow_html=True)
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em'> • Continuously stayed updated with new developments and trends in statistical analysis and software packages.</ul></div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write('')
                st.write(' ')
            with st.container(border=True):
                st.write(' ')
                st.write(' ')
                st.write("""<div style= 'text-align: left;font-size: 1.5em;font-weight: bold'> Skills & Tools Utilized:</div>""",unsafe_allow_html=True)
                st.write('')
                st.write("""<div style= 'text-align: justify;font-size: 1.5em'> • Python | Jupyter Notebook |  MS Excel | Data Wrangling | Data Visualization | Hypotheses Testing | Design of Experiments | Statistical Modellling | Statistical Data Analysis | Reporting and Communication | Pandas | Numpy | Seaborn | Matplotlib | Scipy | Statsmodels | Pingouin. </div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write(' ')




# EDUCATION SECTION
elif st.session_state.section == 'EDUCATION':


   
    with st.container(border=True):
        
        st.markdown("<h2 style='text-align: center; font-weight: bold;font-size: 3em;'>• M.Sc Statistics - Bharathiar University </h2>", unsafe_allow_html=True)
        st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 10px; margin-right: 10px;'>
            <span style='text-align: left; font-weight: bold; font-size: 2em;'>• Coimbatore, Tamil Nadu</span>
            <span style='text-align: right; font-weight: bold; font-size: 2em;'>• 2021 - 2023</span>
            </div>
            """, unsafe_allow_html=True)
        st.write("""<div style= 'text-align: left;font-size: 2em;font-weight: bold;margin-left: 10px;'>* CGPA: 8.61/10</div>""",unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        st.write(' ')
        with st.container(border=True):
            st.write(' ')
            #st.write(' ')
            st.write("""<div style= 'text-align: left;font-size: 1.5em;font-weight: bold'>  Relevant Coursework:</div>""",unsafe_allow_html=True)
            st.write(' ')
            st.markdown("""<div style='text-align: justify; font-size: 1.5em;'>• Descriptive Statistics - Distribution Theory - Sampling Theory - Probability and Measure Theory - 
                 Real Analysis and Linear Algebra - Statistical Estimation Theory - Statistical Quality Control(SQC) - Multivariate
                 Statistical Analysis - Operation Research - Econometrics - Statistical Inference (Hypothesis Testing) - Programming in R - BioStatistics and Survival Analysis - Demography and Vital Statistics - Linear Models and Design of Experiments - Stochastic Processes.</div>""",unsafe_allow_html=True)
            st.write(' ')
            st.write('')
    st.write(' ')
    st.write(' ')

    with st.container(border=True):

        st.markdown("<h2 style='text-align: center; font-weight: bold;font-size: 3em;'>• B.Sc  Statistics - Arignar Anna Govt Arts College </h2>", unsafe_allow_html=True)
        st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 10px; margin-right: 10px;'>
            <span style='text-align: left; font-weight: bold; font-size: 2em;'>• Villupuram, Tamil Nadu</span>
            <span style='text-align: right; font-weight: bold; font-size: 2em;'>• 2018 - 2021</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.write("""<div style= 'text-align: left;font-size: 2em;font-weight: bold;margin-left: 10px;'>* CGPA: 9.39/10</div>""",unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
    st.write(' ')
    st.write(' ')


    with st.container(border=True):

        st.markdown("<h2 style='text-align: center; font-weight: bold;font-size: 3em;'>•  HSC (Biology - Mathematics) - John Dewey Matric Hr.Sec School </h2>", unsafe_allow_html=True)
        st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 10px; margin-right: 10px;'>
            <span style='text-align: left; font-weight: bold; font-size: 2em;'>• Villupuram, Tamil Nadu</span>
            <span style='text-align: right; font-weight: bold; font-size: 2em;'>• 2017 - 2018</span>
            </div>
            """, unsafe_allow_html=True)
        #st.write("""<div style= 'text-align: left;font-size: 2.5em;font-weight: bold;margin-left: 10px;'> Group: Biology-Mathematics</div>""",unsafe_allow_html=True)
        st.write("""<div style= 'text-align: left;font-size: 2em;font-weight: bold;margin-left: 10px;'>* Percentage: 87.25 %</div>""",unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
    st.write(' ')
    st.write(' ')

    with st.container(border=True):

        st.markdown("<h2 style='text-align: center; font-weight: bold;font-size: 3em;'>•  SSLC - The New John Dewey Matric School   (2015 - 2016) </h2>", unsafe_allow_html=True)
        st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 10px; margin-right: 10px;'>
            <span style='text-align: left; font-weight: bold; font-size: 2em;'>• Villupuram, Tamil Nadu</span>
            <span style='text-align: right; font-weight: bold; font-size: 2em;'>• 2015 - 2016</span>
            </div>
            """, unsafe_allow_html=True)
        #st.write("""<div style= 'text-align: left;font-size: 2.5em;font-weight: bold;margin-left: 10px;'> Group: Biology-Mathematics</div>""",unsafe_allow_html=True)
        st.write("""<div style= 'text-align: left;font-size: 2em;font-weight: bold;margin-left: 10px;'>* Percentage: 95.8 %</div>""",unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
    st.write(' ')
    st.write(' ')

 



# SKILLS SECTION
elif st.session_state.section == 'SKILLS':

    with st.container(border=True):
        st.write(' ')
        st.markdown("<h2 style='text-align: left; font-weight: bold;font-size: 3em;'>Tools :</h2>", unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        with st.container(border=True):
            st.write(' ')
            #st.write(' ')
            st.markdown("""<div style= 'text-align: left;font-size: 1.5em;'>* Python | R | SQL | Microsoft Power BI | Jupyter Notebook 
        | IBM SPSS | MINITAB | STATISTICA | Microsoft Excel | MYSQL.</div>""",unsafe_allow_html=True)
            st.write(' ')
            st.write('')
    st.write(' ')
    st.write(' ')


    with st.container(border=True):
        st.write(' ')
        st.markdown("<h2 style='text-align: left; font-weight: bold;font-size: 3em;'>Libraries :</h2>", unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        with st.container(border=True):
            st.write(' ')
            #st.write(' ')
            st.markdown("""<div style= 'text-align: left;font-size: 1.5em;'>*  Pandas | Numpy | Matplotlib | Seaborn | 
                     Plotly | Scipy | Scikit-Learn | TensorFlow | Keras | Statsmodels | Pingouin | Streamlit.</div>""",unsafe_allow_html=True)
            st.write(' ')
            st.write('')
    st.write(' ')
    st.write(' ')

    with st.container(border=True):
        st.write(' ')
        st.markdown("<h2 style='text-align: left; font-weight: bold;font-size: 3em;'>Data Methodologies :</h2>", unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        with st.container(border=True):
            st.write(' ')
            #st.write(' ')
            st.write("""<div style= 'text-align: left;font-size: 1.5em'>* Data Cleaning | Data Analytics | Data Analysis | Exploratory Data Analysis (EDA) | Data Mining | Feature Engineering 
            | Feature Selection Techniques | Data Visualization | Outlier Detection | Correlation Analysis | A/B Testing | Ad Hoc Analysis | Model Evaluation | Model Deployment | Advanced Analytics | Hyperparameter Tuning
        |  Model selection | Model interpretation.</div>""",unsafe_allow_html=True)
            st.write(' ')
            st.write('')
    st.write(' ')
    st.write(' ')   

    with st.container(border=True):
        st.write(' ')
        st.markdown("<h2 style='text-align: left; font-weight: bold;font-size: 3em;'>Expertise :</h2>", unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        with st.container(border=True):
            st.write(' ')
            #st.write(' ')
            st.write("""<div style= 'text-align: left;font-size: 1.5em;'>*  Regression | Classification | Clustering | Predictive Modelling
        | Quantitative Analysis | Statistical Modelling | Deep Learning | Neural Networks
        | CNN | RNN | LSTM | GRU | Bidirectional Models | Time Series Analysis | Forecasting.</div>""",unsafe_allow_html=True)
            st.write(' ')
            st.write('')
    st.write(' ')
    st.write(' ')








# PROJECT SECTION
elif st.session_state.section == 'PROJECTS':

    #project 1: chrono power forecast
    with st.container(border=True):
            st.markdown("<h2 style='text-align: left; font-weight: bold;font-size: 3em;'>• Chrono Power Forecast - Electricity Demand Forecasting for UK Year-2024 </h2>", unsafe_allow_html=True)
            #st.markdown("<h5 style='text-align: left;font-size: 2em;margin-left: 60px;'>Dec 2023 ‑ Jan 2024 </h5>", unsafe_allow_html=True)
            st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 60px; margin-right: 60px;'>
            <span style='text-align: left; font-size: 2em;'>• Self Project</span>
            <span style='text-align: right; font-size: 2em;'>• Dec 2023 ‑ Jan 2024</span>
            </div>
            """, unsafe_allow_html=True)
            st.write('** **') 
            st.image('projects/time series/light.jpg',use_column_width=True)

            on1=st.toggle('Read More')
            if on1:
        #with e3:
                st.write('')
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 2em;font-weight: bold'>  Description :</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Time series analysis and forecasting are crucial tasks in various domains, including energy systems, finance, meteorology, and supply chain management. Time series data consists of observations collected over time, often exhibiting patterns, trends, and seasonal components. Accurate forecasting of future values enables informed decision-making, resource allocation, and proactive planning.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The objective of this project was to analyze historical electricity demand data and apply time series forecasting methods to predict the electricity demand for National Demand (ND), Transmission System Demand (TSD), and England and Wales in 2024. The project utilized data from the National Grid Electricity System Operator (ESO) for Great Britain, which gathered electricity demand information from 2009 to 2023.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size:1.5em;'> • The project involved data preprocessing, visualization, and two main parts. The first part focused on statistical models and the FB-Prophet model, including seasonal decomposition, statistical tests for stationarity, correlation plots, and various time series forecasting models like Simple Exponential Smoothing, Double Exponential Smoothing, Triple Exponential Smoothing, AutoRegressive (AR), Moving Average (MA), AutoRegressive Moving Average (ARMA), Seasonal AutoRegressive Moving Average (SARIMA), and FB-Prophet.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The second part concentrated on deep learning architectures based on sequences, such as Recurrent Neural Networks (RNNs), Bidirectional RNNs, Long Short-Term Memory (LSTM), Bidirectional LSTMs, Gated Recurrent Units (GRUs), Bidirectional GRUs, and hybrid models combining Convolutional Neural Networks (CNNs), LSTMs/GRUs, and Deep Neural Networks (DNNs).</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write(' ')
                p1_link ='https://github.com/itsmesethus/CHRONO-POWER-FORECAST-ELECTRICITY-DEMAND-FORECASTING-FOR-UNITED-KINGDOM-FOR-THE-YEAR-2024-'
                st.link_button(label='Github Link',url=p1_link,help='Project Files Link Is Here!')
                st.write(' ')
                st.write(' ')
            with st.container(border=True):
                st.write(' ')
                st.write(' ')
                st.write("""<div style= 'text-align: left;font-size: 1.4em'> Tools : Python | Pandas | Matplotlib | Seaborn | Scikit-learn | datetime | Statsmodels | TensorFlow | NumPy | Keras | FB-Prophet.</div>""",unsafe_allow_html=True)
                st.write('')
                st.write(' ')
                st.write("""<div style= 'text-align: justify;font-size: 1.4em'> Skills :   Data Preprocessing | Data Visualization | Statistical Modelling | Time Series Analysis | Forecasting | Deep Learning | Sequence Models | Machine Learning. </div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write(' ')
               



   #project 2: cognizant
    with st.container(border=True):
            st.markdown("<h2 style='text-align: left; font-weight: bold;font-size: 3em;'>• Cognizant AI Virtual Internship - Machine Learning for Gala Grocery Retail Pricing </h2>", unsafe_allow_html=True)
            st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 60px; margin-right: 60px;'>
            <span style='text-align: left; font-size: 2em;'>• Self Project</span>
            <span style='text-align: right; font-size: 2em;'>• Sep 2023 ‑ Oct 2023</span>
            </div>
            """, unsafe_allow_html=True)
            st.write('** **') 
            st.image('projects/cognizant/1.jpg',use_column_width=True)

            on2=st.toggle('Read More ')
            if on2:
                st.write('')
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 2em;font-weight: bold''>  Description :</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Gala Groceries, a renowned supermarket chain, partnered with Cognizant to leverage data analytics and machine learning for enhancing customer experience and optimizing business operations. This project showcases the work done to build predictive models and develop machine learning algorithms using Gala Groceries' transactional data. The goal was to uncover valuable insights, improve customer satisfaction, and drive data-driven decision-making in the retail sector.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The project aimed to gain practical experience in data exploration, analysis, and modeling using Python, as well as develop skills in framing business problems, creating strategic plans, and communicating findings. The primary objectives were to build predictive models by combining, transforming, and modeling multiple datasets to address specific business requirements, and to develop machine learning algorithms for predictions, evaluating and improving model performance. Ml Algorithms such as Adaptive Boosting Regressor, HistGradient Boosting Regressor, Bagging Regressor, Radius Neighbors Regressor, and Artificial Neural Networks are utilized here.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The project involved working with a dataset from Gala Groceries that included variables such as timestamps, product IDs, categories, customer types, unit prices, quantities, totals, payment types, average stock percentages, and temperature. The project followed a data science workflow, including data preprocessing, EDA, Feature Engineering, model building, and Model Evaluation.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The project provided insights into customer behaviors, top-selling categories, peak sale timings, and relationships between variables like unit price, quantity, and total sales.</div>""",unsafe_allow_html=True)
                st.write(' ')

                st.markdown("### POWER BI DASHBOARD : COGNIZANT GALA GROCERY STORE")
                st.components.v1.html("""
                <iframe title="COGNIZANT DASHBOARD" src="https://app.powerbi.com/view?r=eyJrIjoiNTRmMzdlYWYtNTY1ZS00ODNlLThkYjgtMWQzYmFkYTdhZDc1IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" style="width: 100%; height: 900px;" frameborder="0" allowFullScreen="true"></iframe> """, height=900,)
                st.write(' ')
                st.write(' ')
                st.markdown("### STREAMLIT APP: COGNIZANT GALA GROCERY STORE APP")
                st.video('projects/cognizant/video app for gala.webm')
                st.write(' ')
                st.write(' ')
                p2_link ='https://github.com/itsmesethus/COGNIZANT-ARTIFICIAL-INTELLIGENCE-VIRTUAL-INTERNSHIP-Machine-Learning-for-Gala-Grocery-Retail-'
                st.link_button(label='Github Link',url=p2_link,help='Project Files Link Is Here!')
                st.write(' ')
                st.write(' ')
#app link should be pasted here
                #gala_app=' //// paste the app link here'
                #st.link_button(label='Gala App Link',url=gala_app,help='Do you want to look the app?')

            with st.container(border=True):
                st.write(' ')
                st.write(' ')
                st.write("""<div style= 'text-align: left;font-size: 1.4em'> Tools : Python | Pandas | Matplotlib | Seaborn | Scikit-learn | datetime | TensorFlow | NumPy | Keras | Power BI | Streamlit.</div>""",unsafe_allow_html=True)
                st.write('')
                st.write(' ')
                st.write("""<div style= 'text-align: justify;font-size: 1.4em'> Skills :   Data Cleaning | Data Preprocessing | Data Visualization | Feature Engineering | Mulivariate Statistical Anlysis | A/B Testing | Deep Learning | Machine Learning | Ensemble Regressors | Model Deployment.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write(' ')



       #project 3: bcg
    with st.container(border=True):
            st.markdown("<h2 style='text-align: left; font-weight: bold;font-size: 3em;'>• BCG Data Science Virtual Internship - Churn Predictive Modelling to Customer Retention</h2>", unsafe_allow_html=True)
            
            st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 60px; margin-right: 60px;'>
            <span style='text-align: left; font-size: 2em;'>• Self Project</span>
            <span style='text-align: right; font-size: 2em;'>• Aug 2023 ‑ Sep 2023</span>
            </div>
            """, unsafe_allow_html=True)
            st.write('** **') 
            st.image('projects/bcg/1.jpg',use_column_width=True)

            on3=st.toggle('Read More  ')
            if on3:
                st.write('')
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 2em;font-weight: bold'>  Description :</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • In today's competitive business landscape, retaining customers is paramount for sustained growth and profitability. Customer churn, or the loss of customers over a given period, poses a significant challenge for companies across various industries. To address this challenge, businesses must proactively identify at-risk customers and implement targeted retention strategies. This project leverages advanced analytics and predictive modeling techniques to uncover underlying patterns and factors contributing to customer churn, enabling businesses to implement proactive measures to retain customers.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The project aimed to Analyze the provided customer data to understand behavior patterns, address data quality issues, and engineer relevant features that capture the underlying characteristics and relationships influencing churn. Develop machine learning models to predict customer churn, evaluate and fine-tune models for accuracy and effectiveness. Interpret model results to identify key factors influencing churn and extract actionable insights to inform customer retention strategies.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Conducted a comprehensive data quality assessment, addressing missing values, inconsistencies, and data formatting issues. Performed  Data Cleaning, EDA, including descriptive statistics, visualizations, and outlier detection, to gain a deep understanding of the data.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Techniques such as feature transformations( Yeo-Johnson Method), encoding, and feature selection were employed to enhance the predictive power of the models. Implemented and evaluated a diverse range of machine learning algorithms, including Artificial Neural Network-Logistic Regression Model, CatBoost Classifier, XGBoost Classifier, GradientBoost Classifier, KNeighbors Classifier. Utilized cross-validation techniques to assess model performance and mitigate overfitting.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size:1.5em;'> • Extracted actionable insights and recommendations to inform customer retention strategies, targeting at-risk customer segments and tailoring retention efforts accordingly. </div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("### POWER BI DASHBOARD: BCG - POWERCO OIL AND GAS CHURN DASHBOARD")
                st.components.v1.html("""
                <iframe title="BCG POWERCO OIL AND GAS CHURN DASHBOARD" src="https://app.powerbi.com/view?r=eyJrIjoiZGJjNzM4NzUtZTVhOS00MWNhLWJjOTYtYzIxN2UyNTc4ZTBiIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" style="width: 100%; height: 800px;" frameborder="0" allowFullScreen="true"></iframe>""", height=800)
                st.write(' ')

#app video
                #st.video('projects/bcg/video app for gala.webm')

                st.write(' ')
                p3_link ='https://github.com/itsmesethus/BCG-DATA-SCIENCE-VIRTUAL-INTERNSHIP---CHURN-BUSTER-PREDICTIVE-MODELING-TO-CUSTOMER-RETENTION-'
                st.link_button(label='Github Link',url=p3_link,help='Project Files Link Is Here!')
                #st.write(' ')
                st.write(' ')
                st.write(' ')
#app link should be pasted here
                #churn_app=' //// paste the app link here'
                #st.link_button(label='Churn App Link',url=churn_app,help='Do you want to look the app?')
                #st.write(' ')


            with st.container(border=True):
                st.write(' ')
                st.write(' ')
                st.write("""<div style= 'text-align: left;font-size: 1.4em'> Tools : Python | Pandas | Matplotlib | Seaborn | Scikit-learn | TensorFlow | NumPy | Keras | Power BI.</div>""",unsafe_allow_html=True)
                st.write('')
                st.write(' ')
                st.write("""<div style= 'text-align: justify;font-size: 1.4em'> Skills :   Data Clenaing | Data Preprocessing | Data Visualization | Feature Transformation | Feature Engineering | Deep Learning | Model Evaluation | Machine Learning | Ensemble Classifiers. </div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write(' ')



    #project 4: Quantium Data Analytics Virtual Internship
    with st.container(border=True):
            st.markdown("<h2 style='text-align: left; font-weight: bold;font-size: 3em;'>• Quantium Data Analytics Virtual Intership - Retail Store Perfomance Analysis And Insights</h2>", unsafe_allow_html=True)
            st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 60px; margin-right: 60px;'>
            <span style='text-align: left; font-size: 2em;'>• Self Project</span>
            <span style='text-align: right; font-size: 2em;'>• May 2023 – Jun 2023</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.write('** **') 
            st.image('projects/quantium/12.jpg',use_column_width=True)

            on4=st.toggle('Read More    ')
            if on4:
                st.write('')
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 2em;font-weight: bold'>  Description :</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • In the ever-evolving landscape of retail, staying ahead of customer demands and preferences is paramount. As a data analytics intern at Quantium, I embarked on an exciting project that delved deep into the world of chips – a beloved snack category that holds a special place in the hearts (and taste buds) of shoppers.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The project's objective was clear: to unravel the intricate patterns and insights hidden within a vast trove of sales data from a major Australian supermarket chain. Armed with a comprehensive dataset spanning 272 stores and covering a one-year period from July 2018 to June 2019, I set out on a mission to unveil the secrets that would shape the supermarket's strategic plan for the chip category in the upcoming half-year.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Checked for missing data and inconsistencies, performed data cleansing using the Z-score method to remove outliers, Ensured data quality, reliability, scalability, and completeness. Created visualizations such as box plots, distribution plots, word clouds, bar plots, pie charts, and line plots. Analyzed trends and patterns related to premium customers, product categories, brand performance, and store sales.
</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Conducted One-Way ANOVA tests to identify significant differences among premium customers, product quantities, and customer life stages. Performed Pearson Correlation analysis to examine the relationship between control stores and trial stores. Applied Independent t-tests to compare means between control stores and trial stores for various performance measures. Compared the performance of control stores and trial stores, providing recommendations for strategic initiatives.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Identified top-performing brands, products, and customer segments within the chip, beverage, and confectionery categories. Analyzed sales trends and customer preferences based on product quantities, life stages, and premium customer segmentation. </div>""",unsafe_allow_html=True)
                st.write(' ')

                #st.markdown("### POWER BI DASHBOARD : COGNIZANT GALA GROCERY STORE")
                #st.components.v1.html("""
                #<iframe title="COGNIZANT DASHBOARD" src="https://app.powerbi.com/view?r=eyJrIjoiNTRmMzdlYWYtNTY1ZS00ODNlLThkYjgtMWQzYmFkYTdhZDc1IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" style="width: 100%; height: 600px;" frameborder="0" allowFullScreen="true"></iframe> """, height=600)
                #st.write(' ')

                #st.video('projects/cognizant/video app for gala.webm')
                st.write(' ')
                
                st.write(' ')
                p4_link ='https://github.com/itsmesethus/QUANTIUM-DATA-ANALYTICS-VIRTUAL-INTERNSHIP-RETAIL-STORE-PERFORMANCE-ANALYSIS-AND-INSIGHTS-'
                st.link_button(label='Github Link',url=p4_link,help='Project Files Link Is Here!')
                st.write(' ')
                st.write(' ')
#app link should be pasted here
                #gala_app=' //// paste the app link here'
                #st.link_button(label='Gala App Link',url=gala_app,help='Do you want to look the app?')

            with st.container(border=True):
                st.write(' ')
                st.write(' ')
                st.write("""<div style= 'text-align: left;font-size: 1.4em'> Tools : Python | Pandas | Numpy | Matplotlib | Seaborn | Scipy.</div>""",unsafe_allow_html=True)
                st.write('')
                st.write(' ')
                st.write("""<div style= 'text-align: justify;font-size: 1.4em'> Skills :   Data Cleaning | Data Preprocessing | Data Visualization | Correlation Analysis| Mulivariate Statistical Anlysis | A/B Testing( Hypotheses Testing). </div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write(' ')


    #project 5: Imdb movie
    with st.container(border=True):
            st.markdown("<h2 style='text-align: left; font-weight: bold;font-size: 3em;'>• IMDB Movie BI Dashboard Perfomance Analysis And Insights</h2>", unsafe_allow_html=True)
            st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 60px; margin-right: 60px;'>
            <span style='text-align: left; font-size: 2em;'>• Self Project</span>
            <span style='text-align: right; font-size: 2em;'>• Jun 2023 – Jul 2023</span>
            </div>
            """, unsafe_allow_html=True)
            st.write('** **') 
            st.image('projects/imdb/1.jpg',use_column_width=True)

            on5=st.toggle('Read More     ')
            if on5:
                st.write('')
                st.write('')
                st.markdown("""<div style='text-align: justify; font-size: 2em;font-weight: bold'>  Description :</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Entertainment industry, movies play a significant role in shaping popular culture and driving box office success. Understanding the factors that contribute to a movie's performance is crucial for filmmakers, studios, and audiences alike. The IMDB Movie Dataset Analysis project aims to provide valuable insights into the characteristics and performance of popular movies by analyzing a comprehensive dataset from IMDb. </div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The project begins by acquiring the IMDb movie dataset, which contains a wealth of information about movies, including their ratings, revenue, genres, cast, and crew members.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Removed inconsistencies from the dataset, ensured for data integrity for data visualization using Power BI. Identifying the top movies based on the number of votes received, providing insights into the most popular and acclaimed films. Calculating average metrics such as Metascore (critical ratings), number of votes, duration, and revenue, giving an overview of the dataset's characteristics. Listing the most popular actors, shedding light on the actors who have garnered the most widespread recognition and etc...</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The Power BI dashboard incorporates various visualizations and interactive elements, allowing users to explore the IMDb movie dataset in an intuitive and engaging manner.  The dashboard presents the key insights and findings from the analysis, including the top movies, average metrics, genre performance, top directors and actors, revenue trends, and genre comparisons based on Metascores. </div>""",unsafe_allow_html=True)
                st.write(' ')

                st.markdown("### POWER BI DASHBOARD: IMDB DASHBOARD")
                st.components.v1.html("""<iframe title="IMDB DASHBOARD" src="https://app.powerbi.com/view?r=eyJrIjoiOGFiZjdlOTItZjZjMS00YzY1LWEwNzItNjNhMWQ3NzdhMDBlIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" style="width: 100%; height: 900px;" frameborder="0" allowFullScreen="true"></iframe>""", height=900)
                st.write(' ')
                st.write(' ')
                p5_link ='https://github.com/itsmesethus/IMDB-MOVIE-POWER_BI-DASHBOARD-'
                st.link_button(label='Github Link',url=p5_link,help='Project Files Link Is Here!')
                st.write(' ')
                st.write(' ')


            with st.container(border=True):
                st.write(' ')
                st.write(' ')
                st.write("""<div style= 'text-align: left;font-size: 1.4em'> Tools : Python | Pandas | NumPy | Power BI.</div>""",unsafe_allow_html=True)
                st.write('')
                st.write(' ')
                st.write("""<div style= 'text-align: justify;font-size: 1.4em'> Skills :   Data Cleaning | Data Preprocessing | Data Visualization. </div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write(' ')




    #project 6: multicalss disease with cnn
    with st.container(border=True):
            st.markdown("<h2 style='text-align: left; font-weight: bold;font-size: 3em;'>• Multiclass Disease Classification of Medical Image Data Using Convolutional Neural Networks</h2>", unsafe_allow_html=True)
        
            st.markdown("""
            <div style='display: flex; justify-content: space-between; margin-left: 60px; margin-right: 60px;'>
            <span style='text-align: left; font-size: 2em;'>• Self Project</span>
            <span style='text-align: right; font-size: 2em;'>• Jan 2023 ‑ Apr 2023</span>
            </div>
            """, unsafe_allow_html=True)
            st.write('** **') 
            st.image('projects/multi diseaase/1.jpg',use_column_width=True)

            on6=st.toggle('Read More        ')
            if on6:
                st.write('')
                st.write('')
               
                st.markdown("""<div style='text-align: justify; font-size: 2em;font-weight: bold'>  Description :</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Accurate disease diagnosis from medical images is critical in healthcare and agriculture. This project leverages convolutional neural networks (CNNs) to develop robust classification models capable of identifying various diseases across multiple domains, including human health, plant pathology, and radiology. By harnessing the power of deep learning techniques like CNNs to extract relevant features from complex image data, this project aims to enhance automated disease diagnosis, ultimately contributing to improved patient outcomes and sustainable agricultural practices.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The project covered four different classification tasks: Binary Class (Pneumonia/Normal), 3 Classes (Potato Plant Leaf Disease), 4 Classes (Corn Plant Leaf Disease), and 8 Classes (GastroIntestinal Diseases in Humans). The objectives were to build accurate CNN models for each task, learn about transfer learning techniques, evaluate model performance, and interpret the results to identify key factors.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The first step involved loading the image datasets, resizing the images to appropriate dimensions, and splitting the data into training, validation, and testing sets. This process included techniques such as image normalization, random horizontal and vertical flips, and random zooming to augment the data.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • Convolutional Neural Network (CNN) models were built using TensorFlow and Keras Sequential APIs. The architectures incorporated convolutional layers for feature extraction, pooling layers for dimensionality reduction, fully connected layers, and appropriate activation functions. Techniques like dropout were employed to prevent overfitting.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • For the 8-Class GastroIntestinal Disease classification task, transfer learning was applied by leveraging the pre-trained VGG19 model weights and fine-tuning the model on the target dataset.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.markdown("""<div style='text-align: justify; font-size: 1.5em;'> • The trained models were evaluated using various metrics such as accuracy, F1 score, precision, and recall. The performance on the validation and test sets was analyzed to assess the models' generalization capabilities.</div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write(' ')
               
        #app link should be pasted here
                #gala_app=' //// paste the app link here'
                #st.link_button(label='Gala App Link',url=gala_app,help='Do you want to look the app?')
                
                p6_link ='https://github.com/itsmesethus/MULTICLASS-DISEASE-CLASSIFICATION-OF-MEDICAL-IMAGE-DATA-USING-CONVOLUTIONAL-NEURAL-NETWORK-'
                st.link_button(label='Github Link',url=p6_link,help='Project Files Link Is Here!')
                st.write(' ')
                st.write(' ')
               
            with st.container(border=True):
                st.write(' ')
                st.write(' ')
                st.write("""<div style= 'text-align: left;font-size: 1.4em'> Tools : Python | Pandas | Numpy | Matplotlib | Seaborn | Scikit-learn | TensorFlow | Keras | OpenCV | Pathlib.</div>""",unsafe_allow_html=True)
                st.write('')
                st.write(' ')
                st.write("""<div style= 'text-align: justify;font-size: 1.4em'> Skills :   Image Preprocessing | Data Visualization | Feature Engineering | Deep Learning | Convlutional Neural Networks | Transfer Learning( with VGG19 )| Model Evaluation. </div>""",unsafe_allow_html=True)
                st.write(' ')
                st.write(' ')



#  CERTIFICATION SECTION
elif st.session_state.section == 'CERTIFICATIONS':
    st.write('')
    st.write("")
    # def load_cerf(folderpath):
    #     images=[]
    #     for filename in os.listdir(folderpath):
    #         if filename.endswith(".jpg"):
    #             images.append(os.path.join(folderpath,filename))
    #     return images

    # folderpath='img certifi'

    # images=load_cerf(folderpath)

    col1,col2,col3,col4= st.columns(4)
  
    with st.container(border=True):
                with col1:
                    st.image('img certifi/1.jpg',use_column_width=True,)
                    st.image('img certifi/1.1.jpg',use_column_width=True,)
                    st.image('img certifi/1.2.jpg',use_column_width=True,)
                    st.image('img certifi/1.3.jpg',use_column_width=True,)
                    st.image('img certifi/1.4.jpg',use_column_width=True,)
                    st.image('img certifi/1.5.jpg',use_column_width=True,)
                    st.image('img certifi/1.6.jpg',use_column_width=True,)
                    st.image('img certifi/1.7.jpg',use_column_width=True,)
                with col2:
                    st.image('img certifi/2.jpg',use_column_width=True,)
                    st.image('img certifi/2.1.jpg',use_column_width=True,)
                    st.image('img certifi/2.2.jpg',use_column_width=True,)
                    st.image('img certifi/2.3.jpg',use_column_width=True,)
                    st.image('img certifi/2.4.jpg',use_column_width=True,)
                    st.image('img certifi/2.5.jpg',use_column_width=True,)
                    st.image('img certifi/2.6.jpg',use_column_width=True,)
                    st.image('img certifi/2.7.jpg',use_column_width=True,)
                with col3:
                    st.image('img certifi/3.jpg',use_column_width=True,)
                    st.image('img certifi/3.1.jpg',use_column_width=True,)
                    st.image('img certifi/3.2.jpg',use_column_width=True,)
                    st.image('img certifi/3.3.jpg',use_column_width=True,)
                    st.image('img certifi/3.4.jpg',use_column_width=True,)
                    st.image('img certifi/3.5.jpg',use_column_width=True,)
                    st.image('img certifi/3.6.jpg',use_column_width=True,)
                    st.image('img certifi/3.7.jpg',use_column_width=True,)
                with col4:
                    st.image('img certifi/4.jpg',use_column_width=True,)
                    st.image('img certifi/4.1.jpg',use_column_width=True,)
                    st.image('img certifi/4.2.jpg',use_column_width=True,)
                    st.image('img certifi/4.3.jpg',use_column_width=True,)
                    st.image('img certifi/4.4.jpg',use_column_width=True,)
                    st.image('img certifi/4.5.jpg',use_column_width=True,)
                    st.image('img certifi/4.6.jpg',use_column_width=True,)
                    st.image('img certifi/4.7.jpg',use_column_width=True,)
                    st.image('img certifi/4.8.jpg',use_column_width=True,)



# CONTACT SECTION
elif st.session_state.section == 'CONTACT':
    with st.container(border=True):
        st.markdown("""
        <style>
        .contact-icon {
            width: 12px;
            height: 12px;
            margin-right: 10px;
        }
        </style>
        """, unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        c1,c2,c3,c4,c5=st.columns(5)

        with c1:
            resume_path = "resume/res.pdf"  # Replace with your actual resume file path
            st.download_button(label="**Download Resume**", data=open(resume_path, 'rb').read(), file_name='Sethu_S_Data_Scientist_resume.pdf', mime='application/pdf',help='Download My Resume Here!',use_container_width=True)

        with c2:
            st.markdown("<a href='mailto:sethus4791@gmail.com' target='_blank'><img src='https://img.icons8.com/color/48/000000/gmail--v2.png' style='vertical-align: middle;'></a> <span style='font-size:20px;'>Email: sethus4791@gmail.com</span>", unsafe_allow_html=True)

        with c3:
                st.markdown("<a href='https://www.linkedin.com/in/sethus4791' target='_blank'><img src='https://img.icons8.com/color/48/000000/linkedin.png' style='vertical-align: middle;'></a> <span style='font-size:20px;'>LinkedIn: www.linkedin.com/in/sethus4791</span>", unsafe_allow_html=True)

        with c4:
            st.markdown("<a href='https://github.com/itsmesethus' target='_blank'><img src='https://img.icons8.com/color/48/000000/github--v1.png' style='vertical-align: middle;'></a> <span style='font-size:20px;'>GitHub: www.github.com/itsmesethus</span>", unsafe_allow_html=True)

        with c5:
            st.markdown("<a href='https://www.kaggle.com/sethu123123' target='_blank'><img src='https://img.icons8.com/?size=48&id=QrYhwpUzAcoy&format=png' style='vertical-align: middle;'></a> <span style='font-size:20px;'>Kaggle: www.kaggle.com/sethu123123</span>", unsafe_allow_html=True)

        st.write(' ')
        st.write(' ')



st.sidebar.text("© 2024 Sethu S's Data Science Portfolio Website")



# [theme]
# primaryColor="#cbe67e"
# backgroundColor="#b2c3ac"
# secondaryBackgroundColor="#d48166"
# textColor="#03120d"
# font="monospace"

# my fav
# [theme]
# primaryColor="#cbe67e"
# backgroundColor="#4c4040"
# secondaryBackgroundColor="#d48166"
# textColor="#d9dedc"
# font="monospace"
