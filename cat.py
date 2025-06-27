from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Apocalypse-19/Vishu-the-Cat')
# Provide a text prompt to the pipeline
prompt = "a photo of a cat, high resolution, detailed"
image = pipeline(prompt).images[0]
# Display the image
image.show()