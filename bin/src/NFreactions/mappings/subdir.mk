################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/NFreactions/mappings/mapping.cpp \
../src/NFreactions/mappings/mappingGenerator.cpp \
../src/NFreactions/mappings/mappingSet.cpp 

OBJS += \
./src/NFreactions/mappings/mapping.o \
./src/NFreactions/mappings/mappingGenerator.o \
./src/NFreactions/mappings/mappingSet.o 

CPP_DEPS += \
./src/NFreactions/mappings/mapping.d \
./src/NFreactions/mappings/mappingGenerator.d \
./src/NFreactions/mappings/mappingSet.d 


# Each subdirectory must supply rules for building sources it contributes
src/NFreactions/mappings/%.o: ../src/NFreactions/mappings/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -I/usr/include/c++/4.8.5 -O3 -c -fmessage-length=0 -std=c++11 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


