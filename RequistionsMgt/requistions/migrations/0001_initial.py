# Generated by Django 3.0.8 on 2020-07-11 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directorate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directorate_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'directorates',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=200, verbose_name='employee name')),
                ('staff_id_num', models.CharField(max_length=20, unique=True, verbose_name='UNRAID No.')),
                ('date_left_org', models.DateField(null=True)),
            ],
            options={
                'verbose_name_plural': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_name', models.CharField(max_length=50, verbose_name='Period name')),
                ('p_number', models.IntegerField(verbose_name='period number')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('num_days', models.IntegerField(default=30, verbose_name='Number of Days')),
                ('p_flag', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'periods',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=100, verbose_name='position')),
            ],
            options={
                'verbose_name_plural': 'positions',
            },
        ),
        migrations.CreateModel(
            name='RateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, verbose_name='Rate Type')),
            ],
            options={
                'verbose_name_plural': 'ratetypes',
            },
        ),
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, verbose_name='Requisition Type')),
            ],
            options={
                'verbose_name_plural': 'requesttypes',
            },
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_made', models.DateTimeField(auto_now_add=True)),
                ('purpose', models.TextField(verbose_name='Purpose')),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requistions.Employee')),
            ],
            options={
                'verbose_name_plural': 'Requisition',
            },
        ),
        migrations.CreateModel(
            name='RequisitionDetailType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'requistiondetailtypes',
            },
        ),
        migrations.CreateModel(
            name='SalaryScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale_name', models.CharField(max_length=100, verbose_name='salary scale name')),
            ],
            options={
                'verbose_name_plural': 'salaryscales',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=100, verbose_name='station')),
            ],
            options={
                'verbose_name_plural': 'stations',
            },
        ),
        migrations.CreateModel(
            name='RequisitionTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_made', models.DateField(db_column='date_made')),
                ('purpose', models.CharField(db_column='purpose', max_length=400)),
                ('total', models.FloatField(db_column='Total')),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='requistions.Employee')),
            ],
            options={
                'verbose_name_plural': 'Requisition totals',
            },
        ),
        migrations.CreateModel(
            name='RequisitionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ndays', models.IntegerField(default=0, verbose_name='Number of days')),
                ('startdate', models.DateField(null=True)),
                ('enddate', models.DateField(null=True)),
                ('rate', models.FloatField(default=0.0, verbose_name='Allowances Rate')),
                ('amount', models.FloatField(default=0.0, verbose_name='Amount')),
                ('detail_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requistions.RequisitionDetailType')),
                ('emp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requistions.Employee')),
                ('period_claimed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requistions.Period')),
                ('requisition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='requistions.Requisition')),
            ],
            options={
                'verbose_name_plural': 'Requisition details',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requistions.Position'),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_scale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requistions.SalaryScale'),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requistions.Station'),
        ),
        migrations.CreateModel(
            name='AllowanceRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('allowance_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requistions.RateType')),
                ('allowance_scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requistions.SalaryScale')),
            ],
            options={
                'verbose_name_plural': 'allowancerates',
            },
        ),
    ]
