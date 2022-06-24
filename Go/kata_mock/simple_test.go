package main

import (
	"github.com/stretchr/testify/mock"
	"testing"

	"github.com/stretchr/testify/suite"
)

type fakeService struct {
	mock.Mock

	address           string
	logging           bool
	extraVerification bool
}

func (s *fakeService) AddValue(cid int, val int, val2 string, val3 string) {
}

func (s *fakeService) GetCurrentValue(cid int) (int, error) {
	args := s.Called(cid)
	return args.Int(0), args.Error(1)
}

type simpleSuite struct {
	suite.Suite
}

func TestSuite(t *testing.T) {
	suite.Run(t, new(simpleSuite))
}

func Test_IfGetCurrentValueIsCalledTwoTimesFromDoServiceCommunication(t *testing.T) {
	service := &fakeService{address: "42.1.55.12:55", logging: true, extraVerification: false}

	service.On("GetCurrentValue", 12555).Return(6464, nil)
	service.On("GetCurrentValue", 121231).Return(42, nil)

	doServiceCommunication(service)

	service.AssertNumberOfCalls(t, "GetCurrentValue", 2)
}

func Test_IfAddValueIsCalledFiveTimesFromDoServiceCommunication(t *testing.T) {
	service := &fakeService{address: "42.1.55.12:55", logging: true, extraVerification: false}

	service.On("GetCurrentValue", 12555).Return(6464, nil)
	service.On("GetCurrentValue", 121231).Return(42, nil)

	service.On("AddValue", 12555, 52, "blarguses", "2x55")
	service.On("AddValue", 12555, 1453, "suffix", "888")
	service.On("AddValue", 121231, 123, "flowers", "4x4c")
	service.On("AddValue", 121231, 1245, "another", "3-wheel")
	service.On("AddValue", 121231, 75, "finally", "131`111")

	service.MethodCalled("AddValue", 12555, 52, "blarguses", "2x55")
	service.MethodCalled("AddValue", 12555, 1453, "suffix", "888")
	service.MethodCalled("AddValue", 121231, 123, "flowers", "4x4c")
	service.MethodCalled("AddValue", 121231, 1245, "another", "3-wheel")
	service.MethodCalled("AddValue", 121231, 75, "finally", "131`111")

	doServiceCommunication(service)

	service.AssertExpectations(t)
	service.AssertNumberOfCalls(t, "AddValue", 5)
}
