from .models import Category,Subject,Syllabus,ContactLeads,Topic,TopicContent
from rest_framework import serializers
from .file_upload import Uploader
from rest_framework.response import Response

# Category Serialization

class Search_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        ref_name = 'CategorySearch'



class Category_Serializer(serializers.ModelSerializer):

    image=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

    def get_image(self, category_instance):
        # Fetch related Uploader objects for the current Category instance
        request = self.context.get('request')
        uploader_objects = Uploader.objects.filter(category=category_instance).order_by('-date_created')
        if uploader_objects.exists():
            data=uploader_objects.first()
            return request.build_absolute_uri(data.category_image.url)
        return f'https://placehold.co/600x400?text={category_instance.name.upper()}'
        
        # Serialize the Uploader objects



# subject Serialization

class Subject_Serializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(read_only=True)
    image=serializers.SerializerMethodField(read_only=True)
    syllabus_url=serializers.SerializerMethodField(read_only=True)
    syllabus_embed=serializers.SerializerMethodField(read_only=True)
    other_files=serializers.SerializerMethodField(read_only=True)


    def get_category_name(self,obj):
        return obj.category.name

    def get_image(self, subject_instance):
        # Fetch related Uploader objects for the current Category instance
        request = self.context.get('request')
        uploader_objects = Uploader.objects.filter(subject=subject_instance).order_by('-date_created')
        if uploader_objects.exists():
            data=uploader_objects.first()
            return request.build_absolute_uri(data.subject_image.url)
        return f'https://placehold.co/600x400?text={subject_instance.name.upper()}'

    def get_syllabus_url(self, subject_instance):
        # Fetch related Uploader objects for the current Category instance
        request = self.context.get('request')
        syllabus_objects = Syllabus.objects.filter(subject=subject_instance).order_by('-date_created')
        if syllabus_objects.exists():
            data=syllabus_objects.first()
            file_url= data.syllabus_file.url
            return request.build_absolute_uri(file_url)
        return None

    def get_syllabus_embed(self,subject_instance):
        syllabus_url=self.get_syllabus_url(subject_instance)
        if syllabus_url:
            return f"<iframe src='{syllabus_url}' width='100%' height='100%'/>"
        return None
    
    def get_other_files(self,subject_instance):
        request = self.context.get('request')
        uploader_objects = Uploader.objects.filter(subject=subject_instance).order_by('-date_created')
        if uploader_objects.exists():
            data=uploader_objects.all()
            urlList=[
                {
             'filename':onefile.subject_files.name.split('/')[-1],
             'url':request.build_absolute_uri(onefile.subject_files.url),
             'created_at':onefile.date_created
            } 
            for onefile in data 
            ]
            return urlList



    class Meta:
        model = Subject
        fields = '__all__'


#Topic Serialization
        
class Topic_SerializerContents(serializers.ModelSerializer):
    # topic_content = TopicContent_Serializer()

    # user_name = serializers.SerializerMethodField(read_only=True)

    # def get_user_name(self,obj):
    #     return obj.user.name
    class Meta:
        model = TopicContent
        fields = ["teacher_name","category","subject","topic", "content","file_upload","date_created","date_updated"]   
        # depth = 1
        # fields = '__all__'

        # def __str__(self):
        #     return self.teacher_name.name
        def get_queryset(self,request,teacher_name,format = None):
            queryset = TopicContent.objects.get(name = teacher_name)

            return Response(queryset)
        

    # def __str__(self):
    #     return self.topic_content          



class Topic_Serializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(read_only=True)
    subject_name = serializers.SerializerMethodField(read_only=True)
    assign_to_name=serializers.SerializerMethodField(read_only=True)
    content=serializers.SerializerMethodField(read_only=True)

    def get_category_name(self,obj):
        return obj.category.name
    
    def get_subject_name(self,obj):
        return obj.subject.name
    
    def get_assign_to_name(self,obj):
        return obj.assign_to.name
    
    def get_content(self,obj):
        try:
            return {
                'status':obj.content.status,
                'id':obj.content.id,
                'message':obj.content.status_message,
                'data':obj.content.content
            }
        except Topic.content.RelatedObjectDoesNotExist:
            return {
                'status':'NON_EXISTENT',
                'id':0,
                'message':'Data Content not created. Ask admin to resolve this error.',
                'data':''
            }
    

    class Meta:
        model =  Topic
        fields = '__all__'
        # fields = ["category","subject","topic_content","added_by","updated_by","status",]

class TopicContent_Serializer(serializers.ModelSerializer):
    # teacher_name= serializers.SerializerMethodField()
    topic=Topic_Serializer(read_only=True)

    class Meta:
        model = TopicContent
        fields = '__all__'




# Syllabus Serializer
class Syllabus_Serializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(read_only=True)
    subject_name = serializers.SerializerMethodField(read_only=True)

    def get_category_name(self,obj):
        return obj.category.name
    
    def get_subject_name(self,obj):
        return obj.subject.name

    class Meta:
        model = Syllabus
        fields = '__all__'        




 # Uploader serializer 

class Uploader_serializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(read_only=True)
    subject_name = serializers.SerializerMethodField(read_only=True)

    def get_category_name(self,obj):
        return obj.category.name
    
    def get_subject_name(self,obj):
        return obj.subject.name
    class Meta:
        model = Uploader
        fields = '__all__'


class Contact_Serializer(serializers.ModelSerializer):

    class Meta:
        model=ContactLeads
        extra_kwargs = {'status': {'required': False}}
        fields='__all__'