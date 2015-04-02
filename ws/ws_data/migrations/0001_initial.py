# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('applicationDate', models.DateField()),
                ('career_stage', models.CharField(max_length=4, choices=[(1, b'phd'), (2, b'ecr'), (3, b'postdoc')])),
                ('dietary_requirements', models.CharField(max_length=2, choices=[(1, b'vegetarian'), (2, b'vegan'), (3, b'gluten free'), (4, b'no mushrooms')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Helpers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('career_stage', models.CharField(max_length=4, choices=[(1, b'phd'), (2, b'ecr'), (3, b'postdoc')])),
                ('dietary_requirements', models.CharField(max_length=2, choices=[(1, b'vegetarian'), (2, b'vegan'), (3, b'gluten free'), (4, b'no mushrooms')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('career_stage', models.CharField(max_length=4, choices=[(1, b'phd'), (2, b'ecr'), (3, b'postdoc')])),
                ('dietary_requirements', models.CharField(max_length=2, choices=[(1, b'vegetarian'), (2, b'vegan'), (3, b'gluten free'), (4, b'no mushrooms')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=3, choices=[(1, b'Australian Antarctic Division'), (2, b'Australian Astronomical Observatory'), (3, b'Australian Catholic University'), (4, b'Australian Institute of Marine Science'), (5, b'Australian National Data Service'), (6, b'Australian National University'), (7, b'Australian Nuclear Science and Technology Organisation'), (8, b'Baker IDI Heart and Diabetes Institute'), (9, b'Bionics Institute'), (10, b'Bureau of Meteorology'), (11, b'Burnet Institute'), (12, b'Charles Sturt University (Albury-Wodonga)'), (13, b'Charles Sturt University (Wagga Wagga)'), (14, b'CSIRO (Clayton)'), (15, b'CSIRO (Hobart)'), (16, b'Curtin University of Technology'), (17, b'Deakin University (Burwood)'), (18, b'Deakin University (Warrnambool)'), (19, b'Edith Cowan University'), (20, b'Federation University (Ballarat)'), (21, b'Fred Hollows Foundation'), (22, b'Griffith University'), (23, b'Griffith University (Gold Coast)'), (24, b'IBM Research'), (25, b'James Cook University'), (26, b'La Trobe University (Bendigo)'), (27, b'La Trobe University (Bundoora)'), (28, b'Macquarie University'), (29, b'Monash Alfred Psychiatry Research Centre'), (30, b'Monash University (Clayton)'), (31, b'Monash University (Parkville)'), (32, b'Murdoch Childrens Research Institute'), (33, b'Museum Victoria'), (34, b'New Zealand eScience Infrastructure'), (35, b'Peter MacCallum Cancer Centre'), (36, b'Queensland Government (Department of Agriculture, Fisheries an Forestry)'), (37, b'Queensland University of Technology'), (38, b'RMIT'), (39, b'Software Sustainability Institute'), (40, b'Southern Cross University (Coffs Harbour)'), (41, b'Swinburne University of Technology (Hawthorn)'), (42, b'University of Adelaide'), (43, b'University of Auckland'), (44, b'University of Canterbury'), (45, b'University of Melbourne (Burnley)'), (46, b'University of Melbourne (Parkville)'), (47, b'University of New England'), (48, b'University of Otago'), (49, b'University of Queensland'), (50, b'University of Southern Queensland'), (51, b'University of Sydney'), (52, b'University of Tasmania (Cradle Coast)'), (53, b'University of Tasmania (Hobart)'), (54, b'University of Technology, Sydney'), (55, b'University of the Sunshine Coast'), (56, b'University of Western Australia'), (57, b'University of Western Sydney'), (58, b'University of Wollongong'), (59, b'UNSW (Canberra)'), (60, b'UNSW (Sydney)'), (61, b'Victoria University (Footscray)'), (62, b'Walter and Eliza Hall Institute of Medical Research')])),
                ('location', models.CharField(max_length=3, choices=[(1, b'Faculty of Architecture, Building and Planning'), (2, b'Melbourne School of Design'), (3, b'Faculty of Arts'), (4, b'Asia Institute'), (5, b'School of Culture and Communication'), (6, b'School of Historical and Philosophical Studies'), (7, b'School of Languages and Linguistics '), (8, b'School of Social and Political Sciences'), (9, b'Graduate School of Humanities and Social Sciences'), (10, b'Faculty of Business and Economics'), (11, b'Melbourne Business School'), (12, b'Melbourne School of Government'), (13, b'The Melbourne Institute'), (14, b'Department of Accounting'), (15, b'Department of Business Administration'), (16, b'Department of Economics'), (17, b'Department of Finance'), (18, b'Department of Management and Marketing'), (19, b'Melbourne Graduate School of Education'), (20, b'Melbourne School of Engineering'), (21, b'Department of Biomedical Engineering'), (22, b'Department of Chemical and Biomolecular Engineering'), (23, b'Department of Computing and Information Systems'), (24, b'Department of Electrical and Electronic Engineering'), (25, b'Department of Infrastructure Engineering'), (26, b'Department of Mechanical Engineering'), (27, b'Melbourne School of Information'), (28, b'Melbourne Law School'), (29, b'Faculty of Medicine, Dentistry and Health Sciences'), (30, b'Melbourne Dental School'), (31, b'Melbourne Medical School'), (32, b'Department of Anatomy and Neuroscience'), (33, b'Department of Biochemistry and Molecular Biology'), (34, b'General Practice and Primary Health Care Academic Centre'), (35, b'Health and Biomedical Informatics Unit'), (36, b'Medical Education Unit'), (37, b'Department of Medicine at Austin Health'), (38, b'Department of Medicine at Royal Melbourne Hospital'), (39, b"Department of Medicine at St Vincent's"), (40, b'Department of Microbiology and Immunology'), (41, b'NorthWest Academic Centre'), (42, b'Department of Obstetrics and Gynaecology'), (43, b'Department of Ophthalmology'), (44, b'Department of Otolaryngology'), (45, b'Department of Pathology'), (46, b'Department of Paediatrics'), (47, b'Pharmacology and Therapeutics'), (48, b'Department of Physiology'), (49, b'Department of Psychiatry'), (50, b'Department of Radiology'), (51, b'Rural Health Academic Centre'), (52, b'Department of Surgery at Austin Health'), (53, b'Department of Surgery at Royal Melbourne Hospital'), (54, b'Department of Surgery at St Vincents'), (55, b'Melbourne School of Health Sciences'), (56, b'Department of Nursing'), (57, b'Department of Physiotherapy'), (58, b'Department of Social Work'), (59, b'Department of Audiology and Speech Pathology'), (60, b'Melbourne School of Population and Global Health'), (61, b'Melbourne School of Psychological Sciences'), (62, b'Florey Institute of Neuroscience and Mental Health'), (63, b'Faculty of Science'), (64, b'School of Botany'), (65, b'School of Chemistry'), (66, b'School of Earth Sciences'), (67, b'Department of Genetics'), (68, b'Department of Mathematics and Statistics'), (69, b'Department of Optometry and Vision Sciences'), (70, b'School of Physics'), (71, b'Department of Zoology'), (72, b'bio21'), (73, b'Faculty of Veterinary and Agricultural Sciences'), (74, b'Faculty of Victorian College of the Arts and Melbourne Conservatorium of Music'), (75, b'Melbourne School of Land and Environment'), (76, b'Department of Agriculture and Food Systems'), (77, b'Department of Forest and Ecosystem Science'), (78, b'Department of Resource Management and Geography'), (79, b'Scholarly Information'), (80, b'VLSCI')])),
                ('department', models.CharField(blank=True, max_length=3, choices=[(1, b'Faculty of Architecture, Building and Planning'), (2, b'Melbourne School of Design'), (3, b'Faculty of Arts'), (4, b'Asia Institute'), (5, b'School of Culture and Communication'), (6, b'School of Historical and Philosophical Studies'), (7, b'School of Languages and Linguistics '), (8, b'School of Social and Political Sciences'), (9, b'Graduate School of Humanities and Social Sciences'), (10, b'Faculty of Business and Economics'), (11, b'Melbourne Business School'), (12, b'Melbourne School of Government'), (13, b'The Melbourne Institute'), (14, b'Department of Accounting'), (15, b'Department of Business Administration'), (16, b'Department of Economics'), (17, b'Department of Finance'), (18, b'Department of Management and Marketing'), (19, b'Melbourne Graduate School of Education'), (20, b'Melbourne School of Engineering'), (21, b'Department of Biomedical Engineering'), (22, b'Department of Chemical and Biomolecular Engineering'), (23, b'Department of Computing and Information Systems'), (24, b'Department of Electrical and Electronic Engineering'), (25, b'Department of Infrastructure Engineering'), (26, b'Department of Mechanical Engineering'), (27, b'Melbourne School of Information'), (28, b'Melbourne Law School'), (29, b'Faculty of Medicine, Dentistry and Health Sciences'), (30, b'Melbourne Dental School'), (31, b'Melbourne Medical School'), (32, b'Department of Anatomy and Neuroscience'), (33, b'Department of Biochemistry and Molecular Biology'), (34, b'General Practice and Primary Health Care Academic Centre'), (35, b'Health and Biomedical Informatics Unit'), (36, b'Medical Education Unit'), (37, b'Department of Medicine at Austin Health'), (38, b'Department of Medicine at Royal Melbourne Hospital'), (39, b"Department of Medicine at St Vincent's"), (40, b'Department of Microbiology and Immunology'), (41, b'NorthWest Academic Centre'), (42, b'Department of Obstetrics and Gynaecology'), (43, b'Department of Ophthalmology'), (44, b'Department of Otolaryngology'), (45, b'Department of Pathology'), (46, b'Department of Paediatrics'), (47, b'Pharmacology and Therapeutics'), (48, b'Department of Physiology'), (49, b'Department of Psychiatry'), (50, b'Department of Radiology'), (51, b'Rural Health Academic Centre'), (52, b'Department of Surgery at Austin Health'), (53, b'Department of Surgery at Royal Melbourne Hospital'), (54, b'Department of Surgery at St Vincents'), (55, b'Melbourne School of Health Sciences'), (56, b'Department of Nursing'), (57, b'Department of Physiotherapy'), (58, b'Department of Social Work'), (59, b'Department of Audiology and Speech Pathology'), (60, b'Melbourne School of Population and Global Health'), (61, b'Melbourne School of Psychological Sciences'), (62, b'Florey Institute of Neuroscience and Mental Health'), (63, b'Faculty of Science'), (64, b'School of Botany'), (65, b'School of Chemistry'), (66, b'School of Earth Sciences'), (67, b'Department of Genetics'), (68, b'Department of Mathematics and Statistics'), (69, b'Department of Optometry and Vision Sciences'), (70, b'School of Physics'), (71, b'Department of Zoology'), (72, b'bio21'), (73, b'Faculty of Veterinary and Agricultural Sciences'), (74, b'Faculty of Victorian College of the Arts and Melbourne Conservatorium of Music'), (75, b'Melbourne School of Land and Environment'), (76, b'Department of Agriculture and Food Systems'), (77, b'Department of Forest and Ecosystem Science'), (78, b'Department of Resource Management and Geography'), (79, b'Scholarly Information'), (80, b'VLSCI')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('other', models.CharField(max_length=60, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('dob', models.DateField(null=True, blank=True)),
                ('gender_identity', models.CharField(default=b'o', max_length=2, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'o', b'Other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=2, choices=[(1, b'HD'), (2, b'D'), (3, b'C'), (4, b'P')])),
                ('career_stage', models.CharField(max_length=4, choices=[(1, b'phd'), (2, b'ecr'), (3, b'postdoc')])),
                ('attendance', models.BooleanField(default=False)),
                ('dietary_requirements', models.CharField(max_length=2, choices=[(1, b'vegetarian'), (2, b'vegan'), (3, b'gluten free'), (4, b'no mushrooms')])),
                ('organisation', models.ForeignKey(to='ws_data.Organisation')),
                ('person', models.ForeignKey(to='ws_data.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('date_held', models.DateField()),
                ('teaching_hours', models.IntegerField()),
                ('catering', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='students',
            name='workshop',
            field=models.ForeignKey(to='ws_data.Workshop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='organisation',
            field=models.ForeignKey(to='ws_data.Organisation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='person',
            field=models.ForeignKey(to='ws_data.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='workshop',
            field=models.ForeignKey(to='ws_data.Workshop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpers',
            name='organisation',
            field=models.ForeignKey(to='ws_data.Organisation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpers',
            name='person',
            field=models.ForeignKey(to='ws_data.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpers',
            name='workshop',
            field=models.ForeignKey(to='ws_data.Workshop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicants',
            name='organisation',
            field=models.ForeignKey(to='ws_data.Organisation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicants',
            name='person',
            field=models.ForeignKey(to='ws_data.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicants',
            name='workshop',
            field=models.ForeignKey(to='ws_data.Workshop'),
            preserve_default=True,
        ),
    ]
