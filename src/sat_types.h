/*******************************************************************************************
 * AUTHOR :     Andrew Hendrix
 * AUTHOR :     Jared Potter
 * AUTHOR :     Leland Stenquist
 * AUTHOR :     Taylor Wilson
 *
 * DATE :       October 24, 2015
 *
 * PURPOSE :    Written for CS 5959 Writing Solid Code, Fall 2015
 *              University of Utah
 */
#ifndef SAT_TYPES_H
#define SAT_TYPES_H

#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

/*******************************************************************************************
 * Color codes for printing to stdout.
 */
#ifndef WIN32
#define KGRN  "\x1b[32m"
#define KCYN  "\x1B[36m"
#define KRED  "\x1B[31m"
#define RESET "\033[0m"
#else
//Windows doesn't support ANSI color standards, so I'm basically removing the functionality on Windows
#define KGRN "DEBUG-GREEN:"
#define KCYN "DEBUG-CYAN :"
#define KRED "DEBUG-RED  :"
#define RESET ""
#endif
#define SATISFIABLE()   { printf("SATISFIABLE\n");   }
#define UNSATISFIABLE() { printf("UNSATISFIABLE\n"); }
#define ERROR()         { printf("ERROR\n");         }

/*******************************************************************************************
 * NAME :             LOG
 *
 * DESCRIPTION :      Prints to stdout if binary was compiled with -DDEBUG. This 
 *                    automatically appends "\n" to the input string.
 * INPUTS :
 *      PARAMETERS :   
 *          char*     str         The string to print to stdout.
 *          int       color       [0 => default], [1 => green], [2 => cyan], [3 => red]
 */
#ifdef DEBUG
#define LOG(str, color) { \
  switch (color)          \
  {                       \
    case 1:               \
      printf(KGRN);       \
      break;              \
    case 2:               \
      printf(KCYN);       \
      break;              \
    case 3:               \
      printf(KRED);       \
      break;              \
    default:              \
      NULL;               \
  }                       \
  printf(str);            \
  printf("\n");           \
  printf(RESET);          \
}
#else
#define LOG(str, color) { /* DO NOTHING */ }
#endif

/*******************************************************************************************
 * NAME :             INPUT
 *
 * DESCRIPTION :      INPUT contains the parsed data values that are ready to be solved.
 *
 * CONTENTS :
 *    int**    data              An array of arrays containing individual clauses of data values.
 *    int      nbcluases         The number of clauses in the file.
 *    int*     clause_lengths    An array containing the length of each clause.
 *    int      nbvars            The maximum and minimum (negated) value in a clause.
 *    int*     pos_val_sums      The number of each variable that is positive
 *    int*     neg_val_sums      The number of each variable that is negative
 *
 */
typedef struct input
{
  int** data;
  int   nbclauses;
  int*  clause_lengths;
  int   nbvars;
  int*  pos_val_sums;
  int*  neg_val_sums;
} INPUT;

#include "optimize.h"
#include "input.h"
#include "solve.h"


#endif 
