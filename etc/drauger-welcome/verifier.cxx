/*
 * verifier.cxx
 * 
 * Copyright 2019 Thomas Castleman <contact@draugeros.org>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
#include <random>
#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	//make list of URLS
	string list[10] = {"https://cygoverify.draugeros.com/cattleloop.php", "https://cygoverify.draugeros.com/devoteranch.php", "https://cygoverify.draugeros.com/earwaxdip.php", "https://cygoverify.draugeros.com/fraudboat.php", "https://cygoverify.draugeros.com/houseplantflight.php", "https://cygoverify.draugeros.com/nailtheorist.php", "https://cygoverify.draugeros.com/pleasenose.php", "https://cygoverify.draugeros.com/progressivetrouser.php", "https://cygoverify.draugeros.com/tippeasant.php", "https://cygoverify.draugeros.com/varietyamputate.php"};
	//set length since C++ doesn't have the ability to count these things
	int list_len = 9;
	//seed random number generator
	std::random_device rd;
 	std::mt19937 eng(rd());
 	//set distribution of integers
 	std::uniform_int_distribution<> distr(0, list_len);
 	//get a random integer
 	int picked = distr(eng);
 	//figure out which URL in the array "list" it corrosponds to
 	string URL = list[picked];
 	//create command string
 	string COMMAND = "/usr/bin/xdg-open " + URL;
 	//convert string to array of chars
 	int len = COMMAND.length();
 	char run[len + 1];
 	strcpy(run, COMMAND.c_str());
 	//open the appropriate URL in the default web browser
 	system(run);
 	
}
