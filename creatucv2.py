from docxtpl import DocxTemplate

doc = DocxTemplate("template.docx")
context = { 'full_name' : "Alfredo Gama Zapata" ,
			'summaryOfBio': "I am the CEO of Voice123, the world’s first and largest online marketplace for professional voice overs.  At Voice123, I spearhead a widely diverse and fully-remote team that has set itself the task of crafting the future of the voiceover industry.\n\nI am an entrepreneurial historian who loves board games, scuba diving, cycling, and doing my bit to change the world for the better. \n\nAt BoardGameBio we are building a tool for competive nerding. Check it out!",
			'strengths1': "Leadership",
			'strengths2': "Strategy",
			'strengths3': "Project Management",
			'strengths4': "Political Advise",
			'strengths5': "Fundraising",
			'strengths6': "Recruitment"
			}
doc.render(context)
doc.save("generated_doc.docx")