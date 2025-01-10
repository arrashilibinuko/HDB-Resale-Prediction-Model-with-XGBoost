# # Create a histogram using Seaborn
# plt.figure(figsize=(8, 5))
# sns.histplot(filtered_data['resale_pricePersqm'], 
#              bins=int((filtered_data['resale_pricePersqm'].max() - filtered_data['resale_pricePersqm'].min()) / 50), 
#              kde=False, 
#              color='blue')
# plt.xlabel("Resale Price per sqm", fontsize=9)
# plt.ylabel("Count", fontsize=9)
# plt.title("Fig.1: A Histogram of the Resale Price in the Sample", fontsize=10, style='italic', loc='center')
# plt.show()

# # Interactive version using Plotly
# fig = px.histogram(
#     filtered_data, 
#     x="resale_pricePersqm", 
#     nbins=int((filtered_data['resale_pricePersqm'].max() - filtered_data['resale_pricePersqm'].min()) / 50), 
#     title="Fig.1: A Histogram of the Resale Price in the Sample",
#     labels={"resale_pricePersqm": "Resale Price per sqm"},
#     color_discrete_sequence=["blue"]
# )
# fig.update_layout(
#     title_font_size=10,
#     xaxis_title_font_size=9,
#     yaxis_title_font_size=9,
#     title_font_family="Arial",
#     title_x=0.5  # Center-align title
# )
# fig.show()