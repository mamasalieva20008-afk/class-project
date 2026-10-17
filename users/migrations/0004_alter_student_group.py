
from django.db import migrations, models
import django.db.models.deletion


def copy_group_names(apps, schema_editor):
    Student = apps.get_model('users', 'Student')
    Group = apps.get_model('academics', 'Group')
    db = schema_editor.connection.alias

    for student in Student.objects.using(db).all().iterator():
        old_name = student.old_group
        group = None

        if old_name:
            group = Group.objects.using(db).filter(name=old_name).first()

        student.group_id = group.pk if group else None
        student.save(using=db, update_fields=['group'])


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
        ('users', '0003_alter_student_admission_year_alter_student_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='group',
            new_name='old_group',
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='students',
                to='academics.group',
                verbose_name='Учебная группа',
            ),
        ),
        migrations.RunPython(
            copy_group_names,
            migrations.RunPython.noop,
        ),
        migrations.RemoveField(
            model_name='student',
            name='old_group',
        ),
    ]
