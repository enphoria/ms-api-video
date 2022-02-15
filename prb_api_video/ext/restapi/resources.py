from flask import abort, jsonify, request
from flask_restful import Resource
from flask_simplelogin import login_required

from prb_api_video.models import Person
from prb_api_video.models import SubjectInterest
from prb_api_video.request import RequestSendMessage
from prb_api_video.consume import Consume

from sqlalchemy.orm import join

from moviepy.editor import *

import json
import os
import datetime


class PersonResource(Resource):
    def get(self):
        persons = Person.query.all()  or abort(204)
        print(persons)
        return jsonify(
            {"persons": [person.to_dict() for person in persons]}
        )

class SendMessageResource(Resource):
    def post(self):
        try:
            obj = json.loads(str(json.dumps(request.get_json())), object_hook=lambda d: RequestSendMessage(**d))
            persons = Person.query.filter(SubjectInterest.name==obj.interest) or abort(204)

            dateNow = datetime.datetime.now()
            dateNow = dateNow.strftime("%Y") + dateNow.strftime("%m") + dateNow.strftime("%d")
            for person in persons:
                if person.subject_interest.name == obj.interest:
                    resultPath = "video/results/result_"+dateNow+"_"+person.name+"_"+person.subject_interest.name+".mp4"
                    clipName = VideoFileClip(person.person_video.path_video)
                    clipIniciative = VideoFileClip(person.subject_interest.path_video)
                    clips = [clipName, clipIniciative]
                    clipsResult = concatenate_videoclips(clips)
                    clipsResult.write_videofile(resultPath, temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")
                    responseVideo = Consume(resultPath,str(person.cellphone))
                    responseVideo.sendVideo()
            return jsonify(
                {"prueba": [person.to_dict() for person in persons]}
            )
        except Exception as e:
	        print(str(e))
        abort(400)


