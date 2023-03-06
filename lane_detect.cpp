#define _CRT_SECURE_NO_WARNINGS
#include <string>
#include <opencv2\opencv.hpp>
#include<iostream>
#include <algorithm>
#include <time.h>
#include<vector>
#include<string>
#include<fstream>
using namespace std;
using namespace cv;


void lane_detect()
{
	VideoCapture capture("E:\\opencv\\lanedetect\\videos\\test2.mp4");
	Mat frame, hsv, mask, edges;
	vector<Vec4f> lines;
	while (capture.read(frame))
	{
		//GaussianBlur(frame, frame, Size(5, 5), 0);
		cvtColor(frame, hsv, COLOR_BGR2HSV);
		inRange(hsv, Scalar(7, 0, 96), Scalar(18, 15, 206), mask);
		Canny(mask, edges, 300, 350);
		//rho�G�ͦ��姤?������?�y�B?�C
		// theta�G�ͦ��姤?�����רB?�A�@��O�k / 180�C
		//	threshold�G�n��??�� �@?��?�һݳ̤֪�����?��?�C
		//	minLineLength�G�q?�� 0�A��̧ܳC?�q��?�סA��???�w??�u��?�q�N����Q??�X?�C
		//	maxLineGap�G�q?�� 0�A��??�P�@��?�O?��??���_?���̤j���Z�áC
		HoughLinesP(edges, lines, 1, CV_PI / 180.0, 50, 150, 1000);
		for (int i = 0; i < lines.size(); i++)
		{
			Vec4f hline = lines[i];
			line(frame, Point(hline[0], hline[1]), Point(hline[2], hline[3]), Scalar(0, 255, 0), 5);
		}
		imshow("frame", frame);
		imshow("mask", mask);
		int key = waitKey(35);
		if (key == 27)
		{
			break;
		}

	}

}